from selenium.webdriver.common.by import By
from Clawler.Driver import webDriver
from tools.TitleFormatter import find_closest_match
import requests
import time
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

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

def get_basic_info_by_id(id):
    url = f"https://movie.douban.com/subject/{id}/"
    print(url)
    resp = requests.get(url, headers=headers)
    # find div with id="info" using bs4
    soup = BeautifulSoup(resp.text, "html.parser")
    info = soup.find_all("div", id="info")[0]
    print(info.text)
    pairs = info.text.split("\n")
    pairs = list(map(lambda x: x.split(":"), pairs))
    # 去空值
    pairs = list(filter(lambda x: len(x) == 2, pairs))
    # 去空格
    pairs = list(map(lambda x: [x[0].strip(), x[1].strip()], pairs))
    # 转为字典
    pairs = dict(pairs)
    return pairs
