from selenium.webdriver.common.by import By


class PageElements:
    """管理页面内的所有元素"""

    # 要修改的联系人
    people = (By.XPATH, '//*[contains(@text,"selenium")]')
    # 修改按钮
    update_button = (By.ID, "com.android.contacts:id/menu_edit")
    # 姓名输入框
    name = (By.CLASS_NAME, "android.widget.EditText")
    # 返回上一层按钮
    butt = (By.CLASS_NAME, "android.widget.ImageButton")
    # 搜索结果
    data = (By.ID, "com.android.contacts:id/large_title")

    """设置 页面"""
    # WLAN
    # 更多
    setting_more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")
    """更多 页面"""
    # 移动网络
    more_network_btn_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")
    # 飞行模式
    """移动网络 页面"""
    # 首选网络类型
    network_type_btn_xpath = (By.XPATH, "//*[contains(@text,'首选网络类型')]")
    # 选择”2G“
    type_select_btn_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    # 获取当前页面的所有信息（用来断言）
    page_text_id = (By.ID, "android:id/summary")
    # 网络运营商
