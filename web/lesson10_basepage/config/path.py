# 管理项目下的路径
import os
# 获取当前文件的路径
config_path = os.path.abspath(__file__)
print("config_path:",config_path)

# config 目录
config_dir = os.path.dirname(config_path)
print("config_dir:",config_dir)
# lesson9 项目路径
root_dir = os.path.dirname(config_dir)
print("root_dir:",root_dir)
# 获取 data 目录路径

data_dir = os.path.join(root_dir,'data')
print("data_dir",data_dir)

if not os.path.exists(config_dir):
    os.mkdir(config_dir)
 # yaml 配置文件的路径
yaml_file = os.path.join(config_dir,'config.yaml')
print("yaml_file:",yaml_file)

