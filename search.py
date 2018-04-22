# -*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup  
from selenium import webdriver
import urllib.request
import urllib
import socket
import time

def search(keyword,driver):
        url_keyword = urllib.request.quote(keyword)  
        url = "http://www.tianyancha.com/search?key=%s&checkFrom=searchBox" %url_keyword    
        driver.get(url)
        time.sleep(4)
        driver.page_source

        url =driver.find_element_by_xpath("//a[contains(@href,'http://www.tianyancha.com/company/')]").get_attribute('href')   
        return url
