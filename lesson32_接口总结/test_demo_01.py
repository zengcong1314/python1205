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

def test_visit_api(mocker):
    expected = 2
    mocker.patch('requests.request',return_value=2)
    actual = visit_api('post',
                       'a',
                       {"name": "yuz"})
    assert expected == actual
