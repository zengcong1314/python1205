import pytest
import requests
from common.excel_handler import ExcelHandler
from config import path
import os
#from common.helper import generate_new_phone
#from middleware.handler import Handler
from middleware.handler import Handler
# TODO:路径处理
# log_file = os.path.join(path.logs_path,'demo.txt')
# print(log_file)
# logger = get_log(file=log_file)



#import logging
# 获取excel文件的路径
# excel_file = os.path.join(path.data_path,'demo.xlsx')
# data =ExcelHandler(excel_file).read_dict('register')
data = Handler.excel.read_dict('register')
@pytest.mark.parametrize("test_info",data)
def test_register_01(test_info):
    # actual_url = 'http://api.lemonban.com/futureloan/member/register'
    # actual_method = 'POST'
    # actual_json = {"mobile_phone":"","pwd":""}
    # actual_headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    # expected = 2
    # 元组要控制索引
    # actual_url = test_info[3]
    # actual_method = test_info[6]
    # actual_json = test_info[4]
    # actual_headers = test_info[5]
    # expected = test_info[7]
    # 字典取值
    actual_url = test_info['url']
    actual_method = test_info['method']
    actual_json = test_info['json']
    actual_headers = test_info['headers']
    expected = test_info['expected']
    # 读取 test_info['json'],
    # 如果存在 # new_phone,
    if '#new_phone#' in actual_json:
        # 生成手机号码 13789456789 generate_new_phone
        mobile_phone = Handler().generate_new_phone()
    # 替换为new_phone
        actual_json = actual_json.replace('#new_phone#',mobile_phone)
    # 通过这种方法，密码不一定知道，最好写入白名单
    if '#exist_phone#' in actual_json:
        pass
    # 传入都是字符串
    res = requests.request(method=actual_method,
                           url = Handler.yaml_config['host'] + actual_url,
                           headers = eval(actual_headers),
                           json=eval(actual_json))
    res_body = res.json()
    print(res_body)
    try:
        assert res_body['code'] == expected
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        # excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('register',
                    str(res_body),
                    row=int(test_info['case_id']) + 1,
                    column=9)
        if res_body['code'] == expected:
            excel.write('register','True',row=int(test_info['case_id']) + 1,column=8)
        else:
            excel.write('register', 'False', row=int(test_info['case_id']) + 1, column=8)

# 数据驱动
# Excel存储用例
# 封装 logger
# 配置文件的编写
# 报告
# 程序入口
# 夹具
# 结果发送钉钉
# 手机号码动态变化



