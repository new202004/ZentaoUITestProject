# 判断禅道是否成功
import HTMLTestRunner
import os
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver


class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()


    def tearDown(self) -> None:  # 测试清理   浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        """验证我的地盘菜单能否正确链接"""
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        # actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        # self.assertEqual(actual_result, '测试人员1', '禅道登录用例执行失败')  # 方法一
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH, '//span[@class="user-name"]'), '测试人员1') # 方法二
        self.driver.find_element(By.XPATH, '//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is(" 我的地盘 - 禅道"))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MenuLinkCase('test_my_link'))
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = open('../../report/%s_%s.html' % (__name__,now_time), 'wb')
    html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='新梦想测试', description='测试描述')
    html_runner.run(suite)
