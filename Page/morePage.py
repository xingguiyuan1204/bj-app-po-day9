from Base.base import Base
from Page.element_page import ElementPage


class MorePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_mobile_bth(self):
        # 点击移动网络按钮
        self.click_ele(ElementPage.more_mobile_btn_xpath)
