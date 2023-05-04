# --coding:utf-8--
import requests
from bs4 import BeautifulSoup
import selenium
import json
from lxml import etree
from Driver import webDriver
from selenium.webdriver.common.by import By
from time  import sleep

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


# 测试 吴京id = 956786
res = mtime_actor_favoriteRating(956786)
print(res)






