import yaml

from lesson12.common.base import BasePage


def test_case(get_driver):
    """运行测试用例"""
    driver = get_driver
    d = BasePage(driver)
    # 打开关键字驱动的表，yaml
    file=r'D:\zengcong\py37\web\lesson12\test\test_add_class.yaml'
    with open(file,encoding='utf-8') as f:
        steps = yaml.safe_load(f)
    for step in steps:
        action = step['action']
        # 要使用的参数：goto,click,fill
        method = getattr(d,action)
        # 要使用的参数：url,locator
        params = step['params']
        # 调用basepage的方法
        method(**params)
