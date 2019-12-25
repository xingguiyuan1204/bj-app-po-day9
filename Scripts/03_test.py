import pytest
import os, sys

sys.path.append(os.getcwd())  # 把当前文件路径添加到python搜索路径
from Base.page import Page
from Base.getDriver import get_android_driver


class Test_03:

    def setup_class(self):
        # 声明我们的driver对象
        self.driver = get_android_driver('com.android.settings', '.Settings')
        # 实例化统一入口类的对象
        self.page = Page(self.driver)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    def test_01(self):
        # 点击更多按钮
        self.page.get_setting_page().click_more_btn()

        # 点击移动网络按钮
        self.page.get_morepage_page().click_mobile_bth()
        # 选择2G网络
        self.page.get_mobilepage_page().click_mobile_2G()

        # 获取页面的文本内容
        text = self.page.get_mobilepage_page().get_mobile_text()
        # 断言
        assert "2G" in text


if __name__ == '__main__':
    pytest.main(["01_test_search.py"])
