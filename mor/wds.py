#! /user/bin/env python
# coding:utf-8
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://wds.modian.com/ranking_list?pro_id=5901")
time.sleep(1)

# 滚滑轮到页面最下方，每1s下移一次，一共下移10次
def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
execute_times(10)