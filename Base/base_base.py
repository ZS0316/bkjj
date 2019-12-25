# 导包
import time

from appium import webdriver


def get_driver(pag, act):
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": pag,
        "appActivity": act,
        "resetKeyboard": True,  # 解决输入中文的问题
        "unicodeKeyboard": True
    }

    # 创建驱动对象
    return webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                            desired_capabilities=capabilities)
