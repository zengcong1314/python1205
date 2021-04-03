import yaml
from web.lesson9_ddt.config.path import yaml_file
def read_yaml(fpath):
    """fpath:yaml 文件的路径"""
    with open(fpath,encoding='utf-8') as f:
        # 读取yaml 当中数据
        data = yaml.safe_load(f)
        return data

# 获取yaml 配置项
yaml_config = read_yaml(yaml_file)

# if __name__ == '__main__':
#     result = read_yaml('D:\zengcong\py37\web\lesson9_ddt\config\config.yaml')
#     print(result)