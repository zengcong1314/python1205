import pytest
from jsonpath import jsonpath
import base64
import requests
from Crypto.Cipher import DES
from middleware.handler import Handler

@pytest.fixture(scope='module')
def get_key():
    url = Handler.yaml_config['host'] + '/api/poros-authcenter/secret/'+ Handler.yaml_config['username']
    res = requests.request('get',url)
    res = res.json()
    secretKey = res['data']
    secretKey = bytes(secretKey, encoding="utf8")
    print(type(secretKey))
    return  {"secretKey":secretKey}

@pytest.fixture(scope='module')
def encrypt(get_key):
    pwd = Handler.yaml_config['password']
    __IV = b'\x01\x02\x03\x04\x05\x06\x07\x08'  # __IV = chr(0)*8
    pad = 8 - len(pwd) % 8
    padStr = ""
    for i in range(pad):
        padStr = padStr + chr(pad)
    pwd = pwd + padStr
    cipher = DES.new(get_key['secretKey'],DES.MODE_CBC,__IV)
    pwd = pwd.encode('utf-8')
    encryptPwd = cipher.encrypt(pwd)
    encryptPwd = base64.b64encode(encryptPwd)
    return {"encryptPwd":encryptPwd}

@pytest.fixture(scope='module')
def login(encrypt):
    baseurl = '/api/poros-authcenter/login'
    url = Handler.yaml_config['host'] + baseurl
    data = {"grant_type":"password","isSerialize":"true","username": Handler.yaml_config['username'],"password":encrypt['encryptPwd']}
    res = requests.request('post',url,data=data)
    res_json = res.json()
    # print(res.json())
    accessToken = jsonpath(res_json, '$..accessToken')[0]
    tokenType = jsonpath(res_json, '$..tokenType')[0]
    return {"accessToken": accessToken, "tokenType": tokenType}

@pytest.fixture(scope='module')
def add_app(login):
    headers = {}
    headers['Authorization'] = login['tokenType'] + ' ' + login['accessToken']
    baseurl = '/api/gks-app/v1/app'
    url = Handler.yaml_config['host'] + baseurl
    data = {"name":"接口自动化测试应用zc","icon":"order"}
    # res = requests.request('post',url,data=data)
    res = requests.request('post',url,headers=headers,
                           json=data)
    res_json = res.json()
    app_id = jsonpath(res_json,'$..id')[0]
    return {"app_id":app_id}





#if __name__ == '__main__':
    # print(login_investor())
    # secretKey = get_key('super_admin')
    # print(type(secretKey))
    # secretKey= bytes(secretKey, encoding="utf8")
    # encryptPwd = encrypt(secretKey,'123456')
    # print("加密后的字符串:",encryptPwd)
    # login('super_admin',encryptPwd)
    #

