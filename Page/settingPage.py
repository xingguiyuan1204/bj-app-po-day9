from Base.base import Base
from Page.element_page import ElementPage


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_more_btn(self):
        """点击设置页面更多按钮"""
        self.click_ele(ElementPage.setting_more_btn_xpath)