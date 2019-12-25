from Base.base import Base
from Page.element_page import ElementPage


class SendMessagePage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    #输入收件人
    def input_recipient(self,text):
        self.send_ele(ElementPage.recipient_xpath,text)

    #输入发送的信息
    def input_push_text(self,text1):
        self.send_ele(ElementPage.push_text_xpath,text1)
    #点击发送按钮
    def click_push_text_bth(self):
        self.click_ele(ElementPage.push_text_bth)

    #获取发送的内容
    def get_push_text(self):
        list1 = self.search_eles(ElementPage.old_push_text_xpaths)
        return [i.text for i in list1]
