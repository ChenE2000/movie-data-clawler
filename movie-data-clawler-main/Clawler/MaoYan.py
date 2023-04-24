from selenium.webdriver.common.by import By
from Clawler.Driver import webDriver
from tools.TitleFormatter import find_closest_match
import time

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
    return titles[idx]["id"]