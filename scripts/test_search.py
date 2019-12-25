import os
import pytest
import sys

from Page.update_people import SearchPage

sys.path.append(os.getcwd())

from Base.base_base import get_driver


class TestSearch(object):
    def setup_class(self):
        self.driver = get_driver("com.android.contacts", ".activities.PeopleActivity")
        self.update_n = SearchPage(self.driver)
    # def teardown_class(self):
    #     self.driver.quit()
    @pytest.fixture(autouse=True,scope="class")
    def search_name(self):
        """点击要修改的联系人"""
        self.update_n.click_people()
    @pytest.fixture(autouse=True)
    def test_page_update(self):
        """点击修改按钮"""
        self.update_n.click_update()
    @pytest.mark.parametrize("names",["python","appium","selenium"])
    def test_update(self,names):
        """修改姓名"""
        self.update_n.send_name(names)
        """获取结果断言"""
        assert names in self.update_n.get_result()

# if __name__ == '__main__':
#     pytest.main(["test_search.py"])