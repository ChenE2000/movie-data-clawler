import argparse
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 根据参数返回不同的webdriver
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='local', help='local or remote')

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument('--headless') # 开启无头模式
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920,1080");
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'")

args = parser.parse_args()
if args.mode == "remote":
    webDriver = wb.Remote(
        command_executor="http://chrome:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
        options=chrome_options
    )
else:
    webDriver = wb.Chrome(options=chrome_options)
