import requests
import pytest

def visit_api(method,url,json):
    res = requests.request(method=method,
                           url=url,
                           json=json)
    return res

def test_real_world():
    expected = 2
    actual = visit_api('post',
                       'a',
                       {"name":"yuz"})
    assert expected == actual

# 客户端mocker
def test_visit_api(mocker):
    expected = 2
    mocker.patch('requests.request',return_value=2)
    actual = visit_api('post',
                       'a',
                       {"name": "yuz"})
    assert expected == actual

# 造假的服务器mocker
# 1、选用已经成型的mocker平台 fastmock 2、自己写 参考之前的 3、
# https://www.fastmock.site/#/