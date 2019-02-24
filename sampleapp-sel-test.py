import requests
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=chrome_options)
driver.get('http://34.220.148.168:8888/project-1.0-RAMA/')
example_images = driver.find_elements(By.TAG_NAME, 'img')


if driver.find_elements_by_css_selector("img[src$='images/devops-pic.png'].ng-hide") :
    print("image hidden")
else :
    print("image displayed")


   
src = driver.page_source
text_found = re.search(r'Hello DevOps Engineers and Architects!', src)
print(text_found)
if not text_found :
	print("text not there")
else:
	print("text Found")
	
 
