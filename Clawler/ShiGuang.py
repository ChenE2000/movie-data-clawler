import json
import time
from Driver import webDriver
from selenium.webdriver.common.by import By
from time import sleep

import requests
from selenium.webdriver.common.by import By

from Clawler.Driver import webDriver

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.132 Safari/537.36",

}


def get_top_10_000_movies():
    url = "http://front-gateway.mtime.com/mtime-search/search/unionSearch2"
    batch = []

    for page in range(10):
        print(f"page: {page + 1}")
        req = requests.post(url, data={
            "keyword": "",
            "pageIndex": page + 1,
            "pageSize": 1000,
            "searchType": 0,
            "locationId": 290,
            "genreTypes": "",
            "area": "中国",
            "year": ""
        }, headers=headers).json()
        batch.extend(req["data"]["movies"])
        time.sleep(5)

    return batch

# 输入的是演员的ID，输出是时光网演员的喜爱度
def mtime_actor_favoriteRating(id):
    url = "http://people.mtime.com/ "+ str(id)
    driver = webDriver
    driver.get(url)
    page_text = driver.page_source

    # 通过id 找到平均喜爱度
    favoritate_rating = driver.find_element(By.ID, "finalRating").text

    # 把返回的字符串处理成字典，然后再转成json返回
    r = favoritate_rating.split(" ")
    res = {}
    res[r[0]] = r[1]
    json_res = json.dumps(res,ensure_ascii=False)

    # 关闭drive
    sleep(3)
    driver.quit()

    return json_res

#输入是电影的ID
def mtime_rating(id):
    url = "https://front-gateway.mtime.com/library/movie/detail.api?&movieId="+str(id)

    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    page_text = requests.get(url=url,headers=headers)

    res = page_text.json()

    # 电影名
    name = res['data']['basic']['name']
    # 电影的5项评分
    movieSubItemRatings = res['data']['basic']['movieSubItemRatings']
    # 总评分
    overallRating = res['data']['basic']['overallRating']
    # 评分人数
    ratingCount = res['data']['basic']['ratingCount']
    # 想看人数
    wantToSeeCount = res['data']['basic']['wantToSeeCount']

    dic_res = {
        '电影名':name,
        '评分':movieSubItemRatings,
        '总评分':overallRating,
        '评分人数':ratingCount,
        '想看人数':wantToSeeCount
    }

    res = json.dumps(dic_res,ensure_ascii=False)
    return res

#输入电影的id，输出电影后期制作技术
def mtime_techniques(id):
    url = "https://front-gateway.mtime.com/library/movie/detail.api?&movieId=" + str(id)

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    page_text = requests.get(url=url, headers=headers)

    res = page_text.json()

    techniques = res['data']['basic']['versions']

    dic_res = {
        "后期制作技术":techniques
    }
    res = json.dumps(dic_res, ensure_ascii=False)

    return res



# 输入是电影的ID
def get_movie_rating_info_by_id(id):
    url = "https://front-gateway.mtime.com/library/movie/detail.api?&movieId=" + \
          str(id)

    page_text = requests.get(url=url, headers=headers)

    res = page_text.json()
    # print(res)
    # 电影名
    name = res['data']['basic']['name']
    # 电影的5项评分
    movieSubItemRatings = res['data']['basic']['movieSubItemRatings']
    # 总评分
    overallRating = res['data']['basic']['overallRating']
    # 评分人数
    ratingCount = res['data']['basic']['ratingCount']
    # 想看人数
    wantToSeeCount = res['data']['basic']['wantToSeeCount']

    dic_res = {
        '电影名': name,
        '评分': movieSubItemRatings,
        '总评分': overallRating,
        '评分人数': ratingCount,
        '想看人数': wantToSeeCount
    }

    # res = json.dumps(dic_res,ensure_ascii=False)
    return dic_res


# # 测试  战狼id = 203613
# id = 203613
# res = mtime_rating(id)
# print(res)


# 输入的是演员的ID，输出是时光网演员的喜爱度
def get_celebrity_popularity_by_id(id):
    url = f"http://people.mtime.com/{id}"
    driver = webDriver
    driver.get(url)

    # 通过id 找到平均喜爱度
    favorite_rating = driver.find_element(By.ID, "finalRating").text

    # 把返回的字符串处理成字典，然后再转成json返回
    r = favorite_rating.split(" ")
    res = {}
    res[r[0]] = r[1]

    return json.dumps(res, ensure_ascii=False)


# # 测试 吴京id = 956786
# res = mtime_actor_favoriteRating(956786)
# print(res)


def get_movie_technique_by_id(id) -> list:
    # 输入电影的id，输出电影后期制作技术
    url = "https://front-gateway.mtime.com/library/movie/detail.api?&movieId=" + str(id)

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    page_text = requests.get(url=url, headers=headers)

    res = page_text.json()

    techniques = res['data']['basic']['versions']

    # dic_res = {
    #     "后期制作技术":techniques
    # }
    # res = json.dumps(dic_res, ensure_ascii=False)

    return techniques


if __name__ == "__main__":
    res = get_top_10_000_movies()
    # save to json
    with open("./10_000_movies.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False)
