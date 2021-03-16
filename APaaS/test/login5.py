import base64
import requests
from Crypto.Cipher import DES
def get_key(username):
    url1 = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/secret/' + username
    res = requests.request('get',url1)
    res = res.json()
    res_data = res['data']
    #print(res)
    print('res_data: ' + res_data)
    res_data = bytes(res_data, encoding="utf8")
    return  res_data

#class DESUtil:

    #@staticmethod
def encrypt(s, key):
    #__BLOCK_SIZE_8 = DES.block_size
    __IV = chr(1) + chr(2) + chr(3) + chr(4) + chr(5) + chr(6) + chr(7) + chr(8)  # __IV = chr(0)*8
    __IV = __IV.encode("utf-8")
    cipher = DES.new(key, DES.MODE_CBC, __IV)
    x = 8 - (len(s) % 8)
    if x != 0:
        s = s + chr(x)*x
    s = s.encode("utf-8")
    msg = cipher.encrypt(s)
    msg = base64.b64encode(msg)
    return msg

def decrypt(enStr, key):
    __IV = chr(1) + chr(2) + chr(3) + chr(4) + chr(5) + chr(6) + chr(7) + chr(8)  # __IV = chr(0)*8
    __IV = __IV.encode("utf-8")
    cipher = DES.new(key, DES.MODE_CBC, __IV)
    decryptByts = base64.b64decode(enStr)
    msg = cipher.decrypt(decryptByts)
    paddingLen = msg[len(msg)-1]
    msg = msg[0:-paddingLen]
    return msg

def login(username, pwd):
    url = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/login'
    data = {"grant_type":"password","isSerialize":"true","username": username,"password":pwd}
    res = requests.request('post',url,data=data)
    # res = requests.request('post', url, params=data)
    print(res.json())

if __name__ == '__main__':
    username = "13925210746"
    secretKey = get_key(username)
    print(secretKey)
    encryptPwd = encrypt('ABC_abc1',secretKey)
    #encryptPwd = str(encryptPwd, encoding="utf-8")
    print("加密后的字符串:",encryptPwd)
    login(username,encryptPwd)









