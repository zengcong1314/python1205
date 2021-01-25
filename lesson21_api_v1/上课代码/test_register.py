"""测试注册测试功能
自动化测试用例
模块名称为什么要以test开头，
执行用例，用到pytest框架，pytest框架会自动识别所有自动化测试用例
测试用例函数要以 test_开头

"""
import logging
import requests
def test_register_01():
    """注册用例"""
    #准备测试数据
    actual_url = 'http://api.lemon.ban.com/futureloan/member/register'
    actual_meth = 'POST'
    actual_json = {"mobile_phone":"","pwd":""}
    actual_headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
    expected = 1
    # requests.request(),而不用 post ,更加灵活
    # 访问接口
    res = requests.request(method=actual_meth,
                     url=actual_url,
                     headers=actual_headers,
                     json=actual_json)
    #获取响应体：json
    res_body = res.text
    res_j = res.json()
    print(res_body)
    # 断言,不需要日志记录就不需要try，断言失败时想进行其他操作时，就要try，要不就直接抛出异常，不会执行下面代码了
    try:
        assert res_j['code'] == expected
    except AssertionError as e:
        logging.error("用例失败：{}".format(e))
        # 捕获异常后一定要记得抛出，用例才会失败
        raise e

# 1、有多个测试用例咋办，要用数据驱动 2、excel存储用例 3、封装logger

