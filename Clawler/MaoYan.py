import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Clawler.Driver import webDriver
from tools.TencentOCR import ocr
from tools.TitleFormatter import find_closest_match


def get_celebrity_id_by_name(name) -> int:
    url = f"https://www.maoyan.com/query?kw={name}&type=1"
    driver = webDriver
    driver.get(url)
    time.sleep(2)
    
    # div with class="celebrity-list"
    if len(driver.find_elements(By.CLASS_NAME, "celebrity-list")) == 0:
        print("No such celebrity")
        return -1
    celebrity_list = driver.find_element(By.CLASS_NAME, "celebrity-list")
    # find all li 
    li_s = celebrity_list.find_elements(By.TAG_NAME, "li")
    if len(li_s) == 0:
        print("No such celebrity")
        return -1
    
    # get the first item
    li = li_s[0]
    name_div = li.find_element(By.CLASS_NAME, "item-title")
    
    if name_div.text != name:
        print("No such celebrity")
        return -1
    
    cid = name_div.find_element(By.TAG_NAME, "a").get_attribute('href').split("/")[-1]
    return (cid)
    

def get_celebrity_boxoffice(cid) -> str:
    unit_map = {
        "万": 10000,
        "亿": 100000000
    }
    
    url = f"https://www.maoyan.com/films/celebrity/{cid}"
    print('[猫眼] 爬取票房信息')
    driver = webDriver
    driver.get(url)
    time.sleep(4)

    # find xpath /html/body/div[3]/div/div[2]/div[4]/div[2]/p[2]
    if len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[2]/div[4]/div[2]/p[2]")) == 0:
        print('[猫眼] 无票房信息')
        return -1
    boxoffice = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[4]/div[2]/p[2]")
    if len(boxoffice.find_elements(By.CLASS_NAME, "stonefont")) == 0:
        print('[猫眼] 无票房信息')
        return -1
    figure = boxoffice.find_element(By.CLASS_NAME, "stonefont")
    unit = boxoffice.find_element(By.CLASS_NAME, "unit").text
    # save p_s[1] as base64
    base_64 = figure.screenshot_as_base64
    
    result = ocr(base_64)[0]['DetectedText'].replace(" ", "")
    result = float(result) * unit_map[unit]
    print(f"[猫眼] 票房信息: {result}")
    return result


# def get_celebrity_nomination_award_times(cid) -> tuple:
#     """ 
#     get celebrity nomination and award times
#     return: award_times, nominations_times
#     """
#     url = f"https://www.maoyan.com/films/celebrity/{cid}"
#     driver = webDriver
#     driver.get(url)
#     time.sleep(2)
#     # find nomination times class="about-num"
#     spans = driver.find_elements(By.CLASS_NAME, "about-num")
#     spec = spans[-1].text
#     # （共2次获奖，2次提名）
#     spec = spec.replace("（共", "").replace("次获奖，", ",").replace("次提名）", "")
#     award_times, nominations_times = spec.split(",")

#     return {
#         "获奖次数": int(award_times),
#         "提名次数": int(nominations_times)
#     }

def get_celebrity_awards(cid) -> list:
    driver = webDriver
    url = f"https://www.maoyan.com/films/celebrity/{cid}"
    print('[猫眼] 爬取获奖信息')
    driver.get(url)
    time.sleep(0.5)
    
    # go to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    # find div with class="award-slider"
    if len(driver.find_elements(By.CLASS_NAME, "award-slider")) == 0:
        return []
    award_slider = driver.find_element(By.CLASS_NAME, "award-slider")
    # find all class="item"
    items = award_slider.find_elements(By.CLASS_NAME, "item")
    
    # find div with class="award-detail"
    award_details = driver.find_element(By.CLASS_NAME, "award-detail")
    # find all class="item"
    details = award_details.find_elements(By.CLASS_NAME, "item")
    
    res_list = []
    # 让鼠标悬停在每个item上，使得item显示
    for i in range(len(items)):
        print(f"[猫眼] 爬取第{i+1}/{len(items)}个获奖信息")
        item, detail = items[i], details[i]
        ActionChains(driver).move_to_element(item).perform()
        time.sleep(0.4)
        award_cover = item.find_element(By.TAG_NAME, "img").get_attribute(name="src")
        award_info = item.find_elements(By.TAG_NAME, "p")
        item_basic_info = {
            "获奖封面": award_cover,
            "获奖名称": award_info[0].text,
            "获奖次数": award_info[1].text
        }

        award_spec = []
        li_s = detail.find_elements(By.TAG_NAME, "li")
        for li in li_s:
            infos = li.find_elements(By.TAG_NAME, "div")
            # 取每个div中的text
            infos = tuple(map(lambda x: x.text, infos))
            award_spec.append(infos)
        
        res_list.append({
            "获奖基本信息": item_basic_info,
            "获奖详情": award_spec
        })
    
    return res_list


def get_movie_awards_info_by_id(id) -> list:
    
    driver = webDriver
    driver.get(f"https://www.maoyan.com/films/{id}")
    

    time.sleep(3)
    try:
        more_awards = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/div[3]/div[1]/div[3]/div[1]/a")
    except Exception as e:
        print("[ERROR]无获奖")
        return []
    # print("more_awards", more_awards)
    actions = ActionChains(driver)
    actions.move_to_element(more_awards).click().perform()
    
    # ========================================
    time.sleep(1)
    # scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    ul = driver.find_elements(By.CLASS_NAME, "award-list")
    if len(ul) == 0:
        return []
    ul = ul[-1]
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
    try:
        # find nomination times class="box.red"
        spans = driver.find_elements(By.CLASS_NAME, "box.red")
        spec = spans[0].text
        # （共2次获奖，2次提名）
        spec = spec.replace("票房", "")
        print(spec)
        return spec
    except Exception:
        return 0


if __name__ == "__main__":
    get_profession_films_boxoffice("万里归途")
