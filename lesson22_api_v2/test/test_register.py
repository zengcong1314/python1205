from lesson22_api_v2.common.logger_hander import get_log
from lesson22_api_v2.config import path
import os
# TODO:路径处理
log_file = os.path.join(path.logs_path,'demo.txt')
print(log_file)
logger = get_log(file=log_file)

import requests
#import logging
def test_register():
    actual_url = 'http://api.lemonban.com/futureloan/member/register'
    actual_method = 'POST'
    actual_json = {"mobile_phone":"","pwd":""}
    actual_headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    expected = 2
    res = requests.request(method=actual_method,
                           url = actual_url,
                           headers = actual_headers,
                           json=actual_json)
    res_body = res.json()
    try:
        assert res_body['code'] == expected
    except AssertionError as e:
        logger.error("用例失败：{}".format(e))
        raise e

# 数据驱动
# Excel存储用例
# 封装 logger
# 配置文件的编写
# 报告
# 程序入口
# 夹具
# 结果发送钉钉
# 手机号码动态变化



