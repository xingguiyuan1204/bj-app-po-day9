from Base.base import Base
from Page.element_page import ElementPage


class MobilePage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)


    def click_mobile_2G(self):
        #点击首选网络类型按钮,选择2G
        self.click_ele(ElementPage.mobile_one_network_xpath)
        self.click_ele(ElementPage.mobile_select_2G_btn_xpath)

    def get_mobile_text(self):
        #获取移动网络设置全部文本内容  text
        num = self.search_eles(ElementPage.mobile_get_summary_text_ids)
        return [i.text for i in num]
