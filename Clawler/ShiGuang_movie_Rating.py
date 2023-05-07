import requests
from bs4 import BeautifulSoup
import selenium
import lxml
import json
import re

#输入是电影的ID
def mtime_rating(id):
    url = "https://front-gateway.mtime.com/library/movie/detail.api?&movieId="+str(id)

    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    page_text = requests.get(url=url,headers=headers)

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
        '电影名':name,
        '评分':movieSubItemRatings,
        '总评分':overallRating,
        '评分人数':ratingCount,
        '想看人数':wantToSeeCount
    }

    res = json.dumps(dic_res,ensure_ascii=False)
    return res



# # 测试  战狼id = 203613
# id = 203613
# res = mtime_rating(id)
# print(res)



