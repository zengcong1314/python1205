import pytest
import requests
from common.yaml_handler import yaml_config,user_config
from jsonpath import jsonpath
@pytest.fixture()
def login():
    """登录.得到ID,token,leave_amount"""
    user = {
        "mobile_phone":user_config['investor_user']['phone'],
        "pwd":user_config['investor_user']['pwd']
    }
    res = requests.request(method='POST',
                     url=yaml_config['host'] + '/member/login',
                     headers={"X-Lemonban-Media-Type":"lemonban.v2"},
                     json=user
                     )
    res_json = res.json()
    #token = res_json['data']['token_info']['token']
    #token_type = res_json['data']['token_info']['token_type']

    token = jsonpath(res_json,'$..token')[0]
    token_type = jsonpath(res_json,'$..token_type')[0]
    id = jsonpath(res_json,'$..id')[0]
    leave_amount = jsonpath(res_json,'$..leave_amount')[0]
    token = " ".join([token_type,token])
    #id = res_json['data']['id']
    #leave_amount = res_json['data']['leave_amount']
    # print(token)
    # print(id)
    # print(leave_amount)
    return  {"id":id,"token":token,"leave_amount":leave_amount}

if __name__ == '__main__':
    print(login())
