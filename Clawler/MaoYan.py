from selenium.webdriver.common.by import By
from Clawler.Driver import webDriver
from tools.TitleFormatter import find_closest_match
from tools.TencentOCR import ocr
import time

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


def get_movie_id_by_title(title: str) -> str:
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
    item = driver.find_element(By.CLASS_NAME, "suggest-detail-list")
    a_s = item.find_elements(By.TAG_NAME, "a")

    titles = []
    for a in a_s:
        titles.append({
            "href": a.get_attribute("href"),
            "text": a.text,
            "id": a.get_attribute("href").split("/")[-1]
        })

    idx = find_closest_match(title, list(map(lambda x: x["text"], titles)))
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
