import base64
import requests
import random
def get_key(username):
    url1 = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/secret/' + username
    res = requests.request('get',url1)
    res = res.json()
    res_data = res['data']
    #print(res)
    print('res_data: ' + res_data)
    res_data = bytes(res_data, encoding="utf8")
    return  res_data


from Crypto.Cipher import DES


# 必须是8个字节，也就是 64 位
# 如果是测试，找开发要 key
# def pad(text):
#     n = len(text) % 8
#     s =text + (b' ' * n)
#     return s

class DESUtil:
    __BLOCK_SIZE_8 = BLOCK_SIZE_8 = DES.block_size
    __IV = chr(1) + chr(2) + chr(3) + chr(4) + chr(5) + chr(6) + chr(7) + chr(8) # __IV = chr(0)*8
    __IV = __IV.encode("utf-8")
    @staticmethod
    def encrypt(str, key):
        cipher = DES.new(key, DES.MODE_CBC, DESUtil.__IV)
        x = DESUtil.__BLOCK_SIZE_8 - (len(str) % DESUtil.__BLOCK_SIZE_8)
        if x != 0:
            str = str + chr(x)*x
        str = str.encode("utf-8")
        msg = cipher.encrypt(str)
        # msg = base64.urlsafe_b64encode(msg).replace('=', '')
        msg = base64.b64encode(msg)
        return msg

    @staticmethod
    def decrypt(enStr, key):
        cipher = DES.new(key, DES.MODE_CBC, DESUtil.__IV)
        # enStr += (len(enStr) % 4)*"="
        # decryptByts = base64.urlsafe_b64decode(enStr)
        decryptByts = base64.b64decode(enStr)
        msg = cipher.decrypt(decryptByts)
        paddingLen = msg[len(msg)-1]
        msg = msg[0:-paddingLen]
        return msg

def login(username, pwd):
    url = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/login'
    data = {"grant_type":"password","isSerialize":"true","username": username,"password":pwd}
    res = requests.request('post',url,data=data)
    print(res.json())

if __name__ == '__main__':
    username = "13925210746"
    secretKey = get_key(username)
    print(secretKey)
    encryptPwd = DESUtil.encrypt('ABC_abc1', secretKey)
    decryptPwd = DESUtil.decrypt(encryptPwd, secretKey)
    encryptPwd = str(encryptPwd, encoding="utf-8")
    print("加密：", encryptPwd)
    print(type(encryptPwd))
    print("解密：", decryptPwd)
    login(username, encryptPwd)

    # key = "yx022y68"
    # res = DESUtil.encrypt("ABC_abc1", key)
    # print(res) # ED5wLgc3Mnw=
    # print(DESUtil.decrypt(res, key))






