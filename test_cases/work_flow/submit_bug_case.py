# 验证可提交bug
import random
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common import set_driver, login, config_value


class SubmitBug(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()
        self.title = "登录bug_py_" + str(random.randint(10000, 30000))

    def tearDown(self) -> None:  # 测试清理   浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_submit_bug(self):
        # """验证能提交bug"""
        login.login(config_value.config.user_name, config_value.config.password, self.driver)
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH, '//span[@class="user-name"]'), '测试人员1') # 方法二
        self.driver.find_element(By.XPATH, '//li[@data-id="qa"]').click()
        self.driver.find_element(By.XPATH,
                                 '//a[contains(@href,"/zentao/www/index.php?m=bug&f=browse&productID=1")]').click()
        self.driver.find_element(By.XPATH, '//a[contains(@href,"/zentao/www/index.php?m=bug&f=creat")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@id="product_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="学生成绩管理系统"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="module_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="/年级成绩管理"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="project_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="湖南中医药测试实训"]').click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="v2.0"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="D:开发人员1"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="deadline"]').send_keys('2020-04-08')

        self.driver.find_element(By.XPATH, '//div[@id="type_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="设计缺陷"]').click()

        self.driver.find_element(By.XPATH, '//div[@id="os_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="Windows 7"]').click()

        self.driver.find_element(By.XPATH, '//div[@id="browser_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="IE系列"]').click()

        self.driver.find_element(By.XPATH, '//input[@name="title"]').send_keys(self.title)
        self.driver.find_element(By.XPATH, '//div[@data-type="severity"]').click()
        self.driver.find_element(By.XPATH, '//span[@data-value="4"]').click()

        self.driver.find_element(By.XPATH, '//div[@data-type="pri"]').click()
        self.driver.find_element(By.XPATH, '//span[@class="label label-pri" and @data-value="4"]').click()
        self.content_frame = self.driver.find_element(By.XPATH, '//iframe[@class="ke-edit-iframe"]')
        self.driver.switch_to.frame(self.content_frame)
        self.driver.find_element(By.XPATH, '//body[@class="article-content"]').clear()
        self.driver.find_element(By.XPATH, '//body[@class="article-content"]').send_keys('<p>[步骤]<p>[结果][期望]')
        self.driver.switch_to.default_content()
        time.sleep(1)

        self.element = self.driver.find_element(By.XPATH, '//div[@id="mailto_chosen"]')
        self.driver.execute_script('arguments[0].scrollIntoView();', self.element)
        time.sleep(1)
        self.element.click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//div[@id="mailto_chosen"]/div/ul/li[@title="T:测试用户"]').click()
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        time.sleep(3)

        self.element_title = '//td[@title="%s"]' % self.title
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.element_title))))


if __name__ == '__main__':
    unittest.main(verbosity=2)
