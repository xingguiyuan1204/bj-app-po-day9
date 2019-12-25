import os,sys
sys.path.append(os.getcwd())       #告诉pytest运行前先检索当前路径
import pytest
from Base.getData import get_data

list1 = []
def get_data_test():
    data = get_data("data3.yaml")
    for i in data.values():
        list1.append(tuple(i.values()))
    return  list1

class Test_05:
    @pytest.mark.parametrize("a,b,c",get_data_test())
    def test_01(self,a,b,c):
        print("\n{}+{}={}".format(a,b,c))
        assert a+b == c