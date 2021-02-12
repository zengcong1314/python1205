import pytest
import requests
from middleware.handler import Handler
from common.db_handler import DBHandler
# from common.yaml_handler import yaml_config,user_config
from jsonpath import jsonpath

def login_fuc(phone,pwd):
    user = {
        "mobile_phone": phone,
        "pwd": pwd
    }
    res = requests.request(method='POST',
                           url=Handler.yaml_config['host'] + '/member/login',
                           headers={"X-Lemonban-Media-Type": "lemonban.v2"},
                           json=user
                           )
    res_json = res.json()
    token = jsonpath(res_json, '$..token')[0]
    token_type = jsonpath(res_json, '$..token_type')[0]
    id = jsonpath(res_json, '$..id')[0]
    leave_amount = jsonpath(res_json, '$..leave_amount')[0]
    token = " ".join([token_type, token])
    return {"id": id, "token": token, "leave_amount": leave_amount}

@pytest.fixture()
def login_investor():
    """登录.得到ID,token,leave_amount"""
    user = {
        "mobile_phone":Handler.user_config['investor_user']['phone'],
        "pwd":Handler.user_config['investor_user']['pwd']
    }
    login_data = login_fuc(user['mobile_phone'],user['pwd'])
    # Handler.inverstor_user_id = login_data['id']
    # Handler.inverstor_user_token = login_data['token']
    return login_fuc(user['mobile_phone'],user['pwd'])
    # res = requests.request(method='POST',
    #                  url=Handler.yaml_config['host'] + '/member/login',
    #                  headers={"X-Lemonban-Media-Type":"lemonban.v2"},
    #                  json=user
    #                  )
    # res_json = res.json()
    # #token = res_json['data']['token_info']['token']
    # #token_type = res_json['data']['token_info']['token_type']
    #
    # token = jsonpath(res_json,'$..token')[0]
    # token_type = jsonpath(res_json,'$..token_type')[0]
    # id = jsonpath(res_json,'$..id')[0]
    # leave_amount = jsonpath(res_json,'$..leave_amount')[0]
    # token = " ".join([token_type,token])
    # #id = res_json['data']['id']
    # #leave_amount = res_json['data']['leave_amount']
    # # print(token)
    # # print(id)
    # # print(leave_amount)
    # return  {"id":id,"token":token,"leave_amount":leave_amount}

@pytest.fixture()
def admin_login():
    """管理员登录"""
    user = {
        "mobile_phone": Handler.user_config['admin_user']['phone'],
        "pwd": Handler.user_config['admin_user']['pwd']
    }
    return login_fuc(user['mobile_phone'], user['pwd'])
    # res = requests.request(method='POST',
    #                        url=Handler.yaml_config['host'] + '/member/login',
    #                        headers={"X-Lemonban-Media-Type": "lemonban.v2"},
    #                        json=user
    #                        )
    # res_json = res.json()
    # token = jsonpath(res_json, '$..token')[0]
    # token_type = jsonpath(res_json, '$..token_type')[0]
    # id = jsonpath(res_json, '$..id')[0]
    # leave_amount = jsonpath(res_json, '$..leave_amount')[0]
    # token = " ".join([token_type, token])
    # return {"id": id, "token": token, "leave_amount": leave_amount}
@pytest.fixture()
def loan_login():
    """管理员登录"""
    user = {
        "mobile_phone": Handler.user_config['loan_user']['phone'],
        "pwd": Handler.user_config['loan_user']['pwd']
    }
    return login_fuc(user['mobile_phone'], user['pwd'])

@pytest.fixture()
def add_loan(loan_login):
    headers = {"X-Lemonban-Media-Type":"lemonban.v2",
               "Authorization":loan_login["token"]}
    data = {"member_id":loan_login["id"],"title":"添加项目成功","amount":2000,"loan_rate":18,"loan_term":30,"loan_date_type":2,"bidding_days":10}

    res = requests.request(method="post",
                           url=Handler.yaml_config['host'] + "/loan/add",
                           headers=headers,
                           json=data)
    res_json = res.json()
    loan_id = jsonpath(res_json,'$..id')[0]
    return loan_id

@pytest.fixture()
def db():
    """管理数据库链接的夹具"""
    db_conn = Handler.db
    yield db_conn
    # db_conn.db_colse()

if __name__ == '__main__':
    print(login_investor())
