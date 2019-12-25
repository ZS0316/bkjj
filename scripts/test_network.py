import sys,os
sys.path.append(os.getcwd())

from Base.base_base import get_driver
from Base.page import Page


class TestNetwork:
    def setup_class(self):
        # 初始化driver
        self.driver = get_driver("com.android.settings",".Settings")
        # 实例化统一入口类
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()
    def test01(self):
        # 点击更多
        self.page.get_setting_page().click_more()
        # 点击移动网络设置
        self.page.get_more_page().click_network()
        # 点击首选网络设置
        self.page.get_network_page().click_type()
        assert "2G" in self.page.get_network_page().get_result()

