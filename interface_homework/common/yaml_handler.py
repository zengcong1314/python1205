import yaml
def read_yaml(fpath):
    with open(fpath,encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.SafeLoader)
    return data
