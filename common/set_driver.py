import os
from selenium import webdriver


def set_driver():
    current = os.path.dirname(__file__)
    chrome_path = os.path.join(current, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    return driver