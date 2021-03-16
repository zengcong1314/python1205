import base64
import requests
from Crypto.Cipher import DES
from middleware.handler import Handler
import pytest


# def test_get_key():
#     url = Handler.yaml_config['url'] + '/api/poros-authcenter/secret/'+ Handler.yaml_config['username']
#     res = requests.request('get',url)
#     res = res.json()
#     res_data = res['data']
#     return  res_data


def test_encrypt(get_key):
    __IV = b'\x01\x02\x03\x04\x05\x06\x07\x08'  # __IV = chr(0)*8
    pwd = Handler.yaml_config['password']
    pad = 8 - len(pwd) % 8
    padStr = ""
    for i in range(pad):
        padStr = padStr + chr(pad)
    pwd = pwd + padStr
    cipher = DES.new(get_key['secretKey'],DES.MODE_CBC,__IV)
    pwd = pwd.encode('utf-8')
    encryptPwd = cipher.encrypt(pwd)
    encryptPwd = base64.b64encode(encryptPwd)
    return encryptPwd

def test_login():
    url = Handler.yaml_config['url'] + '/api/poros-authcenter/login'
    data = {"grant_type":"password","isSerialize":"true","username": username,"password":pwd}
    res = requests.request('post',url,data=data)
    # res = requests.request('post', url, params=data)
    print(res.json())

if __name__ == '__main__':
    secretKey = test_get_key('super_admin')
    print(type(secretKey))
    secretKey= bytes(secretKey, encoding="utf8")
    encryptPwd = test_encrypt(secretKey,'123456')
    print("加密后的字符串:",encryptPwd)
    test_login('super_admin',encryptPwd)





