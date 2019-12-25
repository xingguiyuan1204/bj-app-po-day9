import pytest
import os, sys
sys.path.append(os.getcwd())  # 把当前文件路径添加到python搜索路径
from Base.page import Page
from Base.getDriver import get_android_driver


class Test_04:

    def setup_class(self):
        # 声明我们的driver对象
        # com.android.mms /.ui.ConversationList
        self.driver = get_android_driver('com.android.mms', '.ui.ConversationList')
        # 实例化统一入口类的对象
        self.page = Page(self.driver)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()
    @pytest.fixture(scope="class",autouse=True)
    def fun_01(self):
        # 添加信息按钮
        self.page.get_message_page().click_add_message()
        # 输入收件人信息
        self.page.get_sendmessage_page().input_recipient("10050")

    @pytest.mark.parametrize("text",["啦啦啦","哈哈哈","呵呵呵"])
    def test_01(self,text):
        # 输入发送的内容
        self.page.get_sendmessage_page().input_push_text(text)
        # 点击发送按钮
        self.page.get_sendmessage_page().click_push_text_bth()
        # 获取发送完的信息内容
        msg = self.page.get_sendmessage_page().get_push_text()
        assert text in msg



