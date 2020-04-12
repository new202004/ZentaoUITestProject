# 判断禅道是否成功
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver, login, config_value


class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None:  # 测试清理   浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        """使用test01登录禅道"""
        login.login(config_value.config.user_name, config_value.config.password, self.driver)
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH, '//span[@class="user-name"]'), '测试人员1')# 方法二


if __name__ == '__main__':
    unittest.main(verbosity=2)
