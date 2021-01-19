#1、封装 yaml 文件读取为函数；
import yaml
def read_yaml(filename):
    with open (filename,encoding="UTF-8") as f:
        data = yaml.load(f,Loader=yaml.SafeLoader)
        return  data
res = read_yaml("python36.yaml")
print(res)


#2、封装 ini 配置文件读取为函数；
from configparser import ConfigParser
def read_ini(ini_name,section,sheet):
    parser = ConfigParser()
    parser.read(ini_name,encoding="UTF-8")
    value = parser.get(section,sheet)
    return value
res = read_ini("python36.ini",'db','port')
print(res)

