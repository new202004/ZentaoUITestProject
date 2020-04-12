from selenium.webdriver.common.by import By


def login(username, password, driver):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//input[@id="account"]').send_keys(username)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()