from Page.messagePage import MessagePage
from Page.mobilePage import MobilePage
from Page.morePage import MorePage
from Page.sendmessagePage import SendMessagePage
from Page.settingPage import SettingPage


# 实例化对象统一入口类
class Page():
    def __init__(self, driver):
        self.driver = driver

    def get_setting_page(self):
        return SettingPage(self.driver)

    def get_morepage_page(self):
        return MorePage(self.driver)

    def get_mobilepage_page(self):
        return MobilePage(self.driver)

    def get_message_page(self):
        return MessagePage(self.driver)

    def get_sendmessage_page(self):
        return SendMessagePage(self.driver)