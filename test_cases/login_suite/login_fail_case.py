# 判断禅道是否成功
import HTMLTestRunner
import os
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import login, config_value, set_driver


class LoginFailedCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None:  # 测试清理   浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        """使用test01登录禅道失败"""
        login.login(config_value.config.user_name, '111', self.driver)
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()))  # 方法二


if __name__ == '__main__':
    unittest.main(verbosity=2)
