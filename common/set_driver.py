from selenium import webdriver
from common import config_value


def set_driver():
    driver = webdriver.Chrome(executable_path=config_value.config.chrome_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    url = config_value.config.zantao_url
    driver.get(url)
    return driver


if __name__ == '__main__':
    set_driver()

