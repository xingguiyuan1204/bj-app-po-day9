from selenium.webdriver.common.by import By


class ElementPage:
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")

    """设置页面"""
    # 更多
    setting_more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")

    """更多页面"""
    # 移动网络
    more_mobile_btn_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")

    """移动网络设置页面"""
    # 首选网络类型
    mobile_one_network_xpath = (By.XPATH, "//*[contains(@text,'首选网络')]")
    # 2G
    mobile_select_2G_btn_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    # 获取当前页面所有summary信息
    mobile_get_summary_text_ids = (By.ID, "android:id/summary")


    '''信息页面'''
    #添加信息按钮
    add_message_bth = (By.ID,"com.android.mms:id/action_compose_new")

    '''添加信息页面'''
    #收件人
    recipient_xpath = (By.ID,"com.android.mms:id/recipients_editor")
    #发送内容
    push_text_xpath = (By.ID,"com.android.mms:id/embedded_text_editor")
    #发送按钮
    push_text_bth = (By.ID,"com.android.mms:id/send_button_sms")
    #发送完的信息内容
    old_push_text_xpaths = (By.ID,"com.android.mms:id/text_view")
