import pytest
from selenium.webdriver.common.by import By

from Base.base import Base
from Page.page_element import PageElements


class SearchPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_people(self):
        """点击要修改的联系人"""
        self.click_ele(PageElements.people)

    def click_update(self):
        """点击修改按钮"""
        self.click_ele(PageElements.update_button)

    def send_name(self, text):
        """输入要修改的姓名"""
        self.send_ele(PageElements.name, text)
        """点击返回上一层按钮"""
        self.click_ele(PageElements.butt)

    def get_result(self):
        return self.find_eles(PageElements.data)
