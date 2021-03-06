"""路径"""
import os
# 怎么求reports的目录

# 动态获取路径 1与3的区别
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录
root_path = os.path.dirname(config_path)
print(root_path)

# reports 路径
reports_path = os.path.join(root_path,'reports')
print(reports_path)
if not os.path.exists(reports_path):
    os.mkdir(reports_path)

# log 路径
logs_path = os.path.join(root_path,'logs')
if not os.path.exists(logs_path):
    os.mkdir(logs_path)

# data 路径
data_path = os.path.join(root_path,'data')
if not os.path.exists(data_path):
    os.mkdir(data_path)

# yaml路径
yaml_path = os.path.join(root_path,'config')
if not os.path.exists(yaml_path):
    os.mkdir(yaml_path)
