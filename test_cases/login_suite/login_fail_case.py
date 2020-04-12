# 判断禅道是否成功
import HTMLTestRunner
import os
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import set_driver
from common import login


class LoginFailedCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None:  # 测试清理   浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        """使用test01登录禅道失败"""
        login.login('test01', '111')
        # actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        # self.assertEqual(actual_result, '测试人员1', '禅道登录用例执行失败')  # 方法一
        self.assertTrue(WebDriverWait(10).until(EC.alert_is_present())) # 方法二


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginFailedCase('test_login'))
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = open('result_%s.html' % now_time, 'wb')
    html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='新梦想测试', description='测试描述')
    html_runner.run(suite)
