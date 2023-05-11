import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Clawler.Driver import webDriver
from tools.TencentOCR import ocr
from tools.TitleFormatter import find_closest_match


def get_celebrity_boxoffice(cid) -> float:
    url = f"https://www.maoyan.com/films/celebrity/{cid}"
    driver = webDriver
    driver.get(url)
    time.sleep(2)
    # find boxoffice class="cele-index sumBox"
    p_s = driver.find_elements(By.CLASS_NAME, "stonefont")
    # p_s 第一个是粉丝数，第二个是总票房
    # save p_s[1] as base64
    base_64 = p_s[1].screenshot_as_base64
    boxoffice = float(ocr(base_64)[0]['DetectedText'])
    print(boxoffice)
    return boxoffice


def get_celebrity_nomination_award_times(cid) -> tuple:
    """ 
    get celebrity nomination and award times
    return: award_times, nominations_times
    """
    url = f"https://www.maoyan.com/films/celebrity/{cid}"
    driver = webDriver
    driver.get(url)
    time.sleep(2)
    # find nomination times class="about-num"
    spans = driver.find_elements(By.CLASS_NAME, "about-num")
    spec = spans[-1].text
    # （共2次获奖，2次提名）
    spec = spec.replace("（共", "").replace("次获奖，", ",").replace("次提名）", "")
    award_times, nominations_times = spec.split(",")

    return int(award_times), int(nominations_times)


def get_movie_awards(title, id) -> list:
    
    driver = webDriver
    driver.get(f"https://www.maoyan.com/films/{id}")
    
    before = driver.page_source

    
    time.sleep(3)
    more_awards = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/div[3]/div[1]/div[3]/div[1]/a")
    print("more_awards", more_awards)
    actions = ActionChains(driver)
    actions.move_to_element(more_awards).click().perform()
    
    
    # ========================================
    time.sleep(2)
    
    ul = driver.find_elements(By.CLASS_NAME, "award-list")[-1]
    # find all li
    lis = ul.find_elements(By.TAG_NAME, "li")
    awards_list = []
    
    for li in lis:
        # 获取li中第一个div的text =》 award_name
        award_name = li.find_element(By.TAG_NAME, "div").text
        portrait = li.find_element(By.CLASS_NAME, "portrait")
        awards = li.find_element(By.CLASS_NAME, "content")
        
        # portrait img 的src
        portrait_src = portrait.find_element(By.TAG_NAME, "img").get_attribute("src")
        # awards
        award_items = awards.find_elements(By.TAG_NAME, "div")
        
        awards_list.append({
            "award_name": award_name,
            "portrait_src": portrait_src,
            "award_items": list(map(lambda x: x.text, award_items))
        })
    
    return awards_list
            

def get_movie_id_by_title(title: str) -> int:
    url = f"https://www.maoyan.com/films"
    driver = webDriver

    driver.get(url)
    time.sleep(3)

    # find search input
    search_input = driver.find_element(By.CLASS_NAME, "search")
    search_input.send_keys(title)
    time.sleep(2)
    # find search button
    # search_button = driver.find_element(By.CLASS_NAME, "submit")
    # search_button.click()

    # find movie with class="suggest-detail-list"
    items = driver.find_elements(By.CLASS_NAME, "suggest-detail-list")
    # a_s = item.find_elements(By.TAG_NAME, "a")
    a_s = []
    for item in items:
        a_ = item.find_elements(By.TAG_NAME, "a")
        a_s += a_

    titles = []
    for a in a_s:
        titles.append({
            "href": a.get_attribute("href"),
            "text": a.text,
            "id": a.get_attribute("href").split("/")[-1]
        })

    idx = find_closest_match(title, list(map(lambda x: x["text"], titles)))
    if idx is None:
        return None
    # print(titles, titles[idx])
    return int(titles[idx]["id"])


# 通过电影名在猫眼专业版爬取电影票房
def get_profession_films_boxoffice(title: str) -> str:
    """
    input films name
    get films box office
    return: box office xxx亿
    """
    url = f"https://piaofang.maoyan.com/mdb/search?key={title}"
    driver = webDriver
    driver.get(url)
    time.sleep(2)
    # find nomination times class="box.red"
    spans = driver.find_elements(By.CLASS_NAME, "box.red")
    spec = spans[0].text
    # （共2次获奖，2次提名）
    spec = spec.replace("票房", "")
    print(spec)

    return spec


if __name__ == "__main__":
    get_profession_films_boxoffice("万里归途")
