import yaml
data = {"value":123,"name":"赵四","list":{"age":76}}
with open("./write_yaml.yaml","a",encoding="utf-8")as f:
    #写入yaml文件
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)



