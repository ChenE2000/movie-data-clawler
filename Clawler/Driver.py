from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# TODO 根据参数返回不同的webdriver


# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument('--headless') # 开启无头模式


webDriver = webdriver.Chrome(options=chrome_options)

# webDriver = webdriver.Chrome()