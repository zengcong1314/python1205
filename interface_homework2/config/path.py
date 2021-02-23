import os
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
config_path = os.path.dirname(os.path.abspath(__file__))
print(config_path)

root_path = os.path.dirname(config_path)
print(root_path)

data_path = os.path.join(root_path,"data")
print(data_path)
if not os.path.exists(data_path):
    os.mkdir(data_path)

reports_path = os.path.join(root_path,"reports")
print(reports_path)
if not os.path.exists(reports_path):
    os.mkdir(reports_path)

logs_path = os.path.join(root_path,"logs")
print(logs_path)
if not os.path.exists(logs_path):
    os.mkdir(logs_path)

yaml_path = os.path.join(root_path,"config")
print(yaml_path)
if not os.path.exists(yaml_path):
    os.mkdir(yaml_path)