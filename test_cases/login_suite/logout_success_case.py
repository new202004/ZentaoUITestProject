# 判断禅道退出是否成功
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import login, config_value, set_driver


class LoginFailedCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None:  # 测试清理   浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        """退出禅道成功"""
        login.login(config_value.config.user_name, config_value.config.password, self.driver)
        self.driver.find_element(By.XPATH, '//a[@class="dropdown-toggle"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//a[contains(@href,"/zentao/www/index.php?m=user&f=logout")]').click()
        self.assertTrue(EC.title_is(" 用户登录 - 禅道"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
