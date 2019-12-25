from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def find_ele(self, loc, outtime=5, poll_frequency=1):
        return WebDriverWait(self.driver, outtime, poll_frequency).until(lambda x: x.find_element(*loc))

    # 定位一组元素/返回文本信息列表
    def find_eles(self, loc, outtime=5, poll_frequency=1):
        result = WebDriverWait(self.driver, outtime, poll_frequency).until(lambda x: x.find_elements(*loc))
        return [i.text for i in result]

    # 点击操作
    def click_ele(self, loc, outtime=5, poll_frequency=1):
        self.find_ele(loc, outtime, poll_frequency).click()

    # 清空/输入操作
    def send_ele(self, loc, text, outtime=5, poll_frequency=1):
        result = self.find_ele(loc, outtime, poll_frequency)
        result.clear()
        result.send_keys(text)
