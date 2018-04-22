# -*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup  
from selenium import webdriver
import urllib.request
import socket
import time


def name(url,driver):
        driver.get(url)
        time.sleep(4)
        nameList = []
        while nameList == []: 
                nameList = driver.find_elements_by_xpath("//table[@class='table companyInfo-table']/tbody/tr/td/a[@class='ng-binding ng-isolate-scope']")
        print ("公司的股东有:")
        for each in nameList:
                print (each.text)