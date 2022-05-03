import sys

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service("D:\\Hitechs\\Installs\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

def test_score_service(url):
    driver.get(url)
    score = driver.find_element(By.ID, "score")
    if 0 < int(score.text) < 1000:
        return True
    else:
        return False

def main_function():
    try:
        a = test_score_service("http://192.168.56.102:5000")
        if a:
            sys.exit(0)
        else:
            raise selenium.common.exceptions.WebDriverException
    except selenium.common.exceptions.WebDriverException:
        sys.exit(-1)
