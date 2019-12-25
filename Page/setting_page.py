from Base.base import Base
from Page.page_element import PageElements


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_more(self):
        """点击更多"""
        self.click_ele(PageElements.setting_more_btn_xpath)
