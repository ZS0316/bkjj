from Base.base import Base
from Page.page_element import PageElements


class MorePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_network(self):
        """点击移动网络"""
        self.click_ele(PageElements.more_network_btn_xpath)
