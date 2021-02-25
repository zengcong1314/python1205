import json

import pytest
import requests
from middleware.handler import Handler
from jsonpath import jsonpath

@pytest.fixture()
def login():
    user = {"username":Handler.user_config['user']['login_user'],
            "password":Handler.user_config['user']['password']}
    res = requests.request(method='POST',
                           url=Handler.yaml_config['host'] + '/user/login/',
                           json=user)
    res_body = json.loads(res.text)
    token = jsonpath(res_body,'$.token')[0]
    token = 'JWT' + ' ' + token
    user_id = jsonpath(res_body,'$.user_id')[0]

    return {"token":token,"user_id":user_id}

@pytest.fixture()
def add_projects(login):
    headers = {"Authorization":login["token"]}
    data = {"name":"#project_name#","leader":"yuze","tester":"zc","programmer":"keyou","publish_app":"huawei","desc":"desc"}
    data = str(data)
    if "#project_name#" in data:
        project_name = Handler.generate_random_str(6)
        data = data.replace('#project_name#',project_name)
    res = requests.request(method='POST',
                           url=Handler.yaml_config['host'] + "/projects/",
                           headers=headers,
                           json=eval(data))
    res_body = json.loads(res.text)
    project_id = jsonpath(res_body,'$..id')[0]
    return {"project_id":project_id}

@pytest.fixture()
def add_interface(login,add_projects):
    headers = {"Authorization":login["token"]}
    data = {"name":"#interface_name# ","tester":"zc","project_id":"#project_id#","desc":"desc"}
    data = str(data)
    if "#interface_name#" in data:
        interface_name = Handler.generate_random_str(6)
        data = data.replace('#interface_name#',interface_name)
    if "#project_id#" in data:
        project_id = add_projects['project_id']
        data = data.replace('#project_id#',str(project_id))
    res = requests.request(method='POST',
                           url=Handler.yaml_config['host'] + "/interfaces/",
                           headers=headers,
                           json=eval(data))
    res_body = json.loads(res.text)
    interface_id = jsonpath(res_body,'$..id')[0]
    return {"interface_id":interface_id}

@pytest.fixture()
def add_cases(add_interface):
    headers = {"Authorization":login["token"]}
    data = {"name":"#case_name#","interface":{"pid":"#project_id#","iid":"#interface_id#"},"include":{"config":1,"testcases":[1,2]},"autor":"可优","request":"请求数据"}
    data = str(data)
    if "#case_name#" in data:
        cases_name = Handler.generate_random_str(6)
        data = data.replace('#case_name#',cases_name)
    if "#project_id#" in data:
        project_id = add_projects['project_id']
        data = data.replace('#project_id#',project_id)
    if '#interface_id#' in data:
        interface_id = add_interface['interface_id']
        data = data.replace('#interface_id#', interface_id)
    res = requests.request(method='POST',
                           url=Handler.yaml_config['host'] + "/testcases/",
                           headers=headers,
                           json=eval(data))
    res_body = json.loads(res.text)
    project_id = jsonpath(res_body,'$..id')[0]
    return project_id
