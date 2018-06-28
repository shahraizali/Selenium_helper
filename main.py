__author__ = 'Rizwan Hameed'
__date__ = 'December 23, 2017'
"""
Check out my main scraping projects !
https://www.youtube.com/playlist?list=PLh2kzLvQxb76sv7s6aUB6378zy4Tkpzv0
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pythonLib
import os
import datetime
import urllib


#function to start browsing and getting page soup
def request(url, driver):
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)

    return driver


#function to make soup
def make_soup(driver):
    page = driver.page_source
    soup = BeautifulSoup(page, "html5lib")
    return soup


#function to process sub awards extraction
def main(INDEX_URL):
    driver = webdriver.Chrome()
    driver = request(INDEX_URL, driver)
    time.sleep(1)

    
    #driver.quit()


#main function...
def crawl(INDEX_URL):

    main(INDEX_URL)


if __name__ == '__main__':
    start_time = datetime.datetime.now().replace(microsecond=0)
    INDEX_URL = "https://www.hayneedle.com/product/imax-shoelace-and-raffia-woven-baskets-set-of-3.cfm?rNtt=XMA3860"
    crawl(INDEX_URL)
    end_time = datetime.datetime.now().replace(microsecond=0)
    print("Execution Time:")
    print(end_time - start_time)
    
