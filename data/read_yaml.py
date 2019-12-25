import yaml


with open("./data2.yaml","r",encoding="utf-8")as f:
    text = yaml.safe_load(f)
    print(text)