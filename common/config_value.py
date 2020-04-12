import os
import configparser


class ConfigValue:
    def __init__(self):
        self.current_path = os.path.dirname(__file__)
        self.conf_path = os.path.join(self.current_path, '../conf/local_config.ini')
        self.conf = configparser.ConfigParser()
        self.conf_data = self.conf.read(self.conf_path, encoding='utf-8')

    @property
    def zantao_url(self):
        return self.conf.get("zentao", "zentao_url")

    @property
    def user_name(self):
        return self.conf.get("user", "user_name")

    @property
    def password(self):
        return self.conf.get("user", "password")

    @property
    def chrome_path(self):
        return self.conf.get("driver", "chrome_path")


config = ConfigValue()

if __name__ == '__main__':
    zantao_url = config.zantao_url
    user_name = config.user_name
    password = config.password
    chrome_path = config.chrome_path
    print(zantao_url, user_name, password, chrome_path)
