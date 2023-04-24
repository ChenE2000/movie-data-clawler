import requests
from bs4 import BeautifulSoup
import selenium
import lxml
import json
import re

#输入是电影的ID，然后会metadata/ShiGuang目录下,把当前电影的5个评分以json格式放入文件夹中
def mtime_grade(id):
    url = "https://front-gateway.mtime.com/library/movie/detail.api?&movieId="+str(id)

    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    page_text = requests.get(url=url,headers=headers)

    res = page_text.json()

    name = res['data']['basic']['name']

    grade = res['data']['basic']['movieSubItemRatings']

    print(name,grade)
    
    with open("../metadata/ShiGuang/"+name+".json",'w',encoding="utf-8") as fp:
        json.dump(grade,fp,ensure_ascii=False)
        fp.close()


# 测试
# 1战狼
id = 203613
# 2盗梦空间
id1 = 99547
mtime_grade(id)


