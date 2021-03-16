import base64
import requests
import random
def get_key():
    url1 = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/secret/13925210746'
    res = requests.request('get',url1)
    res = res.json()
    res_data = res['data']
    #print(res)
    print(res_data)
    res_data = bytes(res_data, encoding="utf8")
    return  res_data


from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes



# 必须是8个字节，也就是 64 位
# 如果是测试，找开发要 key
# def pad(text):
#     n = len(text) % 8
#     s =text + (b' ' * n)
#     return s

def encrypt(key,data):
    pad = 8 - len(data) % 8
    padStr = ""
    for i in range(pad):
        data = data + chr(pad)
    # data = data + padStr
    # mode = DES.MODE_CBC
    Des_IV = "\1\2\3\4\5\6\7\8"
    cipher = DES.new(key, DES.MODE_CBC,Des_IV)
    iv = cipher.iv
    # plaintext = bytes(data, encoding="utf8")
    plaintext = 'ABC_abc1'.encode('utf-8')
    msg = cipher.encrypt(plaintext)
    #print(msg)
    print('================================')
    msg = base64.b64encode(msg)
    return msg

def decrypt(enStr, key):
    __IV = "\0\0\0\0\0\0\0\0"
    cipher = DES.new(key, DES.MODE_CBC,__IV)
    decryptByts = base64.b64decode(enStr)
    msg = cipher.decrypt(decryptByts)
    paddingLen = ord(msg[len(msg)-1])
    return msg[0:-paddingLen]

def login(pwd):
    url = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/login'
    data = {"grant_type":"password","isSerialize":"true","username":"13925210746","password":pwd}
    res = requests.request('post',url,data=data)
    print(res.json())

if __name__ == '__main__':
    res = get_key()
    print(res)
    res1 = encrypt(res,'ABC_abc1')
    # res2 = decrypt(res1,res)
    res1 = bytes.decode(res1)
    print("加密：",res1)
    print(type(res1))
    # print("解密：", res2)
    login(res1)
    a = random.randint(1,8)
    print(a)






