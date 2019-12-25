from Base.base import Base
from Page.page_element import PageElements


class NetworkType(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_type(self):
        """点击首选网络类型"""
        self.click_ele(PageElements.network_type_btn_xpath)
        """选择2G"""
        self.click_ele(PageElements.type_select_btn_xpath)

    def get_result(self):
        """获取页面所有数据"""
        return self.find_eles(PageElements.page_text_id)
