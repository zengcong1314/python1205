import base64
import requests

def get_key():
    url1 = 'http://kong.poros-platform.10.74.166.198.nip.io/api/poros-authcenter/secret/super_admin'
    res = requests.request('get',url1)
    res = res.json()
    res_data = res['data']
    #print(res)
    #print(res_data)
    return  res_data


from Crypto.Cipher import DES



def encrypt(key,s):
    #__IV = "\0\0\0\0\0\0\0\0"
    cipher = DES.new(key,DES.MODE_CBC)
    iv = cipher.iv
    plaintext = '123456'.encode('utf-8')
    msg = cipher.encrypt(plaintext)
    print(msg)
    print('================================')
    msg = base64.b64encode(msg)
    return msg
    # cipher = DES.new(key, DES.MODE_OFB, iv=iv)
    # a = cipher.decrypt(msg)
    # 后面用 base64
class DESUtil:
    __BLOCK_SIZE_8 = BLOCK_SIZE_8 = DES.block_size
    __IV = b"\1\2\3\4\5\6\7\8" # __IV = chr(0)*8
    @staticmethod
    def encryt2(a, key):
        Des_IV = {1, 2, 3, 4, 5, 6, 7, 8}

        cipher = DES.new(key, DES.MODE_CBC, Des_IV)
        x = DESUtil.__BLOCK_SIZE_8 - (len(a) % DESUtil.__BLOCK_SIZE_8)
        if x != 0:
            a = a + chr(x)*x
        msg = cipher.encrypt(a)
        # msg = base64.urlsafe_b64encode(msg).replace('=', '')
        msg = base64.b64encode(msg)
        return msg



if __name__ == '__main__':
    res = get_key()
    print(type(res))
    res= bytes(res, encoding="utf8")

    # res1 = encrypt(res)
    # print(res1)
    res3 = DESUtil().encryt2('123456',res)
    print(res3)





