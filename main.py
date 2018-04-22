# -*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup  
from selenium import webdriver
import urllib.request
import socket
import time
import search
import name

while True:
        driver = webdriver.PhantomJS(executable_path= r"C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        company = input("请输入查询公司名称(输入quit退出):")
        if (company!="quit"):
                url = search.search(company,driver)
                name.name(url,driver)
                driver.close()
        else:
                break