from selenium.webdriver.common.by import By
from Clawler.Driver import webDriver
from tools.TitleFormatter import find_closest_match
import time
import numpy as np
import json


# 处理2023第一季度数据
def get_actor_2023_Q1(cid) -> tuple:
    url = f"https://www.chinaindex.net/actor/1/{cid}?stageflag=2023-Q1"
    driver = webDriver
    driver.get(url)
    time.sleep(10)
    # find nomination times class="sub-title"
    spans = driver.find_elements(By.CLASS_NAME, "sub-title")
    spec = []
    for i in range(6):
        if i == 2:
            continue
        spec.append(spans[i].text)

    spec[0] = spec[0].replace("2023年第一季度商业价值", "").replace("指数各维度评分如图:", "").replace(" ", "").replace("\n", "")
    name, commercial_value = spec[0].split(":")
    commercial_value = commercial_value.replace(name, "")

    spec[1] = spec[1].replace(name, "").replace("2023年第一季度代言指数: ", "").replace(" ", "").replace("\n", "")
    endorsement_value = spec[1]

    spec[2] = spec[2].replace(name, "").replace("2023年第一季度热度指数: ", "").replace(" ", "").replace("\n", "")
    heat_value = spec[2]

    spec[3] = spec[3].replace(name, "").replace("2023年第一季度口碑指数: ", "").replace("各维度好评率如图", "")
    spec[3] = spec[3].replace("*数据过于稀疏时, 无法计算好评率", "").replace(" ", "").replace("\n", "")
    praise_value = spec[3]

    spec[4] = spec[4].replace(name, "").replace("2023年第一季度专业指数: ", "").replace(" ", "").replace("\n", "")
    major_value = spec[4]

    return float(commercial_value), float(endorsement_value), float(heat_value), float(praise_value), float(major_value)


# 处理2022第一季度数据
def get_actor_2022_Q1(cid) -> tuple:
    url = f"https://www.chinaindex.net/actor/1/{cid}?stageflag=2022-Q1"
    driver = webDriver
    driver.get(url)
    time.sleep(10)
    # find nomination times class="sub-title"
    spans = driver.find_elements(By.CLASS_NAME, "sub-title")
    spec = []
    for i in range(6):
        if i == 2:
            continue
        spec.append(spans[i].text)

    spec[0] = spec[0].replace("2022年第一季度商业价值", "").replace("指数各维度评分如图:", "").replace(" ", "").replace("\n", "")
    name, commercial_value = spec[0].split(":")
    commercial_value = commercial_value.replace(name, "")

    spec[1] = spec[1].replace(name, "").replace("2022年第一季度代言指数: ", "").replace(" ", "").replace("\n", "")
    endorsement_value = spec[1]

    spec[2] = spec[2].replace(name, "").replace("2022年第一季度热度指数: ", "").replace(" ", "").replace("\n", "")
    heat_value = spec[2]

    spec[3] = spec[3].replace(name, "").replace("2022年第一季度口碑指数: ", "").replace("各维度好评率如图", "")
    spec[3] = spec[3].replace("*数据过于稀疏时, 无法计算好评率", "").replace(" ", "").replace("\n", "")
    praise_value = spec[3]

    spec[4] = spec[4].replace(name, "").replace("2022年第一季度专业指数: ", "").replace(" ", "").replace("\n", "")
    major_value = spec[4]

    return float(commercial_value), float(endorsement_value), float(heat_value), float(praise_value), float(major_value)


# 处理2022第二季度数据
def get_actor_2022_Q2(cid) -> tuple:
    url = f"https://www.chinaindex.net/actor/1/{cid}?stageflag=2022-Q2"
    driver = webDriver
    driver.get(url)
    time.sleep(10)
    # find nomination times class="sub-title"
    spans = driver.find_elements(By.CLASS_NAME, "sub-title")
    spec = []
    for i in range(6):
        if i == 2:
            continue
        spec.append(spans[i].text)

    spec[0] = spec[0].replace("2022年第二季度商业价值", "").replace("指数各维度评分如图:", "").replace(" ", "").replace("\n", "")
    name, commercial_value = spec[0].split(":")
    commercial_value = commercial_value.replace(name, "")

    spec[1] = spec[1].replace(name, "").replace("2022年第二季度代言指数: ", "").replace(" ", "").replace("\n", "")
    endorsement_value = spec[1]

    spec[2] = spec[2].replace(name, "").replace("2022年第二季度热度指数: ", "").replace(" ", "").replace("\n", "")
    heat_value = spec[2]

    spec[3] = spec[3].replace(name, "").replace("2022年第二季度口碑指数: ", "").replace("各维度好评率如图", "")
    spec[3] = spec[3].replace("*数据过于稀疏时, 无法计算好评率", "").replace(" ", "").replace("\n", "")
    praise_value = spec[3]

    spec[4] = spec[4].replace(name, "").replace("2022年第二季度专业指数: ", "").replace(" ", "").replace("\n", "")
    major_value = spec[4]

    return float(commercial_value), float(endorsement_value), float(heat_value), float(praise_value), float(major_value)


# 处理2022第三季度数据
def get_actor_2022_Q3(cid) -> tuple:
    url = f"https://www.chinaindex.net/actor/1/{cid}?stageflag=2022-Q3"
    driver = webDriver
    driver.get(url)
    time.sleep(10)
    # find nomination times class="sub-title"
    spans = driver.find_elements(By.CLASS_NAME, "sub-title")
    spec = []
    for i in range(6):
        if i == 2:
            continue
        spec.append(spans[i].text)

    spec[0] = spec[0].replace("2022年第三季度商业价值", "").replace("指数各维度评分如图:", "").replace(" ", "").replace("\n", "")
    name, commercial_value = spec[0].split(":")
    commercial_value = commercial_value.replace(name, "")

    spec[1] = spec[1].replace(name, "").replace("2022年第三季度代言指数: ", "").replace(" ", "").replace("\n", "")
    endorsement_value = spec[1]

    spec[2] = spec[2].replace(name, "").replace("2022年第三季度热度指数: ", "").replace(" ", "").replace("\n", "")
    heat_value = spec[2]

    spec[3] = spec[3].replace(name, "").replace("2022年第三季度口碑指数: ", "").replace("各维度好评率如图", "")
    spec[3] = spec[3].replace("*数据过于稀疏时, 无法计算好评率", "").replace(" ", "").replace("\n", "")
    praise_value = spec[3]

    spec[4] = spec[4].replace(name, "").replace("2022年第三季度专业指数: ", "").replace(" ", "").replace("\n", "")
    major_value = spec[4]

    return float(commercial_value), float(endorsement_value), float(heat_value), float(praise_value), float(major_value)


# 处理年度数据
def get_actor_sum(cid) -> list:

    Q1_2023 = get_actor_2023_Q1(cid)

    Q1_2022 = get_actor_2022_Q1(cid)

    Q2_2022 = get_actor_2022_Q2(cid)

    Q3_2022 = get_actor_2022_Q3(cid)

    Q_sum = (np.array(Q1_2022) + np.array(Q2_2022) + np.array(Q3_2022) + np.array(Q1_2023)) / 4
    Q_sum = Q_sum.tolist()
    return Q_sum


# 通过演员名字获取网页ID
def get_movie_id_by_title(title: str) -> str:
    url = f"https://www.chinaindex.net/search"
    driver = webDriver

    driver.get(url)
    time.sleep(5)

    # find search input
    search_input = driver.find_element(By.CLASS_NAME, "home-search-input")
    search_input.send_keys(title)
    time.sleep(3)

    # find search button
    search_button = driver.find_element(By.CLASS_NAME, "home-search-cancel")
    search_button.click()
    time.sleep(10)

    # find movie with class="flex1.left"
    item = driver.find_element(By.CLASS_NAME, "flex1.left")
    a_s = item.find_elements(By.TAG_NAME, "img")
    # print(len(a_s))
    a_t = item.find_elements(By.TAG_NAME, "h2")
    # print(len(a_t))
    titles = []
    titles.append({
        "href": a_s[0].get_attribute("data-src"),
        "text": a_t[0].text,
        "id": a_s[0].get_attribute("data-src").split("/")[-2]
    })
    # idx = find_closest_match(title, list(map(lambda x: x["text"], titles)))
    # print(titles, titles[idx])
    return int(titles[0]["id"])


if __name__ == "__main__":
    test = ["黄渤", "黄磊"]
    data = []
    for i in range(len(test)):
        id_aiman = get_movie_id_by_title(test[i])
        print(id_aiman)
        Q = get_actor_sum(id_aiman)
        Q.append(test[i])
        print(Q)
        data.append(Q)
    with open("./aiman.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

