# 使用Ubuntu 20.04作为基础镜像
FROM ubuntu:20.04

# 安装Chrome浏览器和Chrome驱动程序
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get install -y chromium-chromedriver && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装Python 3和Selenium库
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install selenium && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录并将TaskManager.py添加到容器中
WORKDIR /app
COPY . /app

# 设置Chrome浏览器的启动选项
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV DISPLAY=:99

# 启动Xvfb虚拟显示器并运行TaskManager.py
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x16 & sleep 3 && python3 TaskManager.py"]
