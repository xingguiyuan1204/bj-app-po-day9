import os

import yaml


def get_data(data_name):
    with open("./data"+os.sep+data_name,"r",encoding="utf-8")as f:
        #解析
        return yaml.safe_load(f)