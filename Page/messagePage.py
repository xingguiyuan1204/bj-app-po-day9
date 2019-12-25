from Base.base import Base
from Page.element_page import ElementPage


class MessagePage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    #点击添加信息按钮
    def click_add_message(self):
        self.click_ele(ElementPage.add_message_bth)