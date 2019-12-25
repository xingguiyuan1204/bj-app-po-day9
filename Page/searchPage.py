
from Base.base import Base
from Page.element_page import ElementPage


class SearchPage(Base,ElementPage):

    def __init__(self, driver):
        Base.__init__(self,driver)  #初始化父类init方法

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(ElementPage.search_btn)

    def search_text(self, text):
        """
        搜索内容
        :param text: 输入文本内容
        :return:
        """
        self.send_ele(ElementPage.search_input, text)

    def ge_search_result(self):
        """
        获取搜索结果
        :return: 列表
        """
        # 定位
        results = self.search_eles(ElementPage.search_result)
        # 返回
        return [i.text for i in results]
