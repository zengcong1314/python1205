"""yaml文件解析

pip install pyyaml
yaml注意两个问题：
- key 后面的冒号：加空格
- 层级要缩进
- 可以用注释 #

yaml 是现在最主流的配置文件 docker，K8S
"""
import yaml

#打开文件
with open("python36.yaml",encoding="UTF-8") as f:
    #加载文件中数据，保存在data中
    data = yaml.load(f,Loader=yaml.SafeLoader)
print(data)
print(data['db']['port'])
print(data['users'][1]['password'])
print(data['users'][0])

# 封装函数