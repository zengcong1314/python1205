from jsonpath import jsonpath
import requests
from middleware.handler import Handler

def test_login(encrypt):
    baseurl = '/api/poros-authcenter/login'
    url = Handler.yaml_config['host'] + baseurl
    data = {"grant_type":"password","isSerialize":"true","username": Handler.yaml_config['username'],"password":encrypt['encryptPwd']}
    res = requests.request('post',url,data=data)
    res_json = res.json()
    print(res.json())
    accessToken = jsonpath(res_json, '$..accessToken')[0]
    tokenType = jsonpath(res_json, '$..tokenType')[0]
    return accessToken,tokenType
