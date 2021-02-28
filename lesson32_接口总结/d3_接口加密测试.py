import requests
import time
from jsonpath import jsonpath
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from base64 import b64encode

def sign(ts,token):
    data = token[:50] + ts
    return data

def encrypt(msg):
    key = '-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedEO3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBrtuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+SkKlZFc8Br7SHtbL2tQIDAQAB-----END PUBLIC KEY-----'
    public_key = RSA.import_key(key)
    cipher = PKCS1_v1_5.new(public_key)
    data = cipher.encrypt(msg.encode())
    return data

def get_sign(ts,token):
    s = token[:50] + ts
    key = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedEO3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBrtuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+SkKlZFc8Br7SHtbL2tQIDAQAB\n-----END PUBLIC KEY-----'
    public_key = RSA.import_key(key)
    cipher = PKCS1_v1_5.new(public_key)
    encrypted_bytes = cipher.encrypt(s.encode())
    return b64encode(encrypted_bytes).decode()

def login():
    user = {
        "mobile_phone":"18211112222",
        "pwd":"12345678"
    }
    res = requests.request(method='post',
                           url='http://api.lemonban.com/futureloan' + '/member/login',
                           headers= {"X-Lemonban-Media-Type":"lemonban.v3"},
                           json=user)
    res_json = res.json()
    token = jsonpath(res_json,'$..token')[0]
    token_type = jsonpath(res_json,'$..token_type')[0]
    id = jsonpath(res_json,'$..id')[0]
    leave_amount = jsonpath(res_json,'$..leave_amount')[0]
    token = " ".join([token_type,token])
    return {"id":id,
            "token":token,
            "leave_amount":leave_amount}

def test_recharge():
    a = login()
    headers = {"X-Lemonban-Media-Type":"lemonban.v3",
               "Authorization":a['token']}

    ts = str(int(time.time()))
    sign = get_sign(ts,a['token'].split(' ')[1])

    data = {"member_id":a['id'],"amount":100,
            "timestamp":ts,
            "sign":sign}

    res = requests.request(url='http://api.lemonban.com/futureloan' + '/member/recharge',
                           method='post',
                           headers=headers,
                           json=data)

    print(res.json())

if __name__ == '__main__':
    test_recharge()

