from selenium.webdriver.common.by import By
from Clawler.Driver import webDriver
from tools.TitleFormatter import find_closest_match
import time


def get_movie_id_by_title(title: str) -> str:
    """ 通过电影标题获取电影ID """
    url = f"https://search.douban.com/movie/subject_search?search_text={title}&cat=1002"
    driver = webDriver
    driver.get(url)
    time.sleep(2)
    # find movie class="item-root"
    items = driver.find_elements(By.CLASS_NAME, "title")

    if len(items) == 0:
        return None
    # extract all href and text of <a> tags
    titles = []
    for item in items:
        try:
            a = item.find_element(By.TAG_NAME, "a")
            titles.append({
                "href": a.get_attribute("href"),
                "text": a.text,
                "id": a.get_attribute("href").split("/")[-2]
            })
        except:
            # skip if no <a> tag
            pass
    
    idx = find_closest_match(title, list(map(lambda x: x["text"], titles)))
    # print(titles[idx])
    return titles[idx]["id"]


