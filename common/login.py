import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import set_driver


def login(username, password):
    driver = set_driver.set_driver()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//input[@id="account"]').send_keys(username)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()