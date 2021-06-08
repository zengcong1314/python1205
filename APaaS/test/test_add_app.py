import json
from jsonpath import jsonpath
import requests
from middleware.handler import Handler
import pytest

data = Handler.excel.read_dict('app')
@pytest.mark.parametrize("info",data)
def test_add_app(info,login):
    if info["json"]:
        if '#app_name#' in info["json"] :
            info["json"] = info["json"].replace('#app_name#',Handler.yaml_config['app']['app_name'])
        if '#icon#' in info["json"]:
            info["json"] = info["json"].replace('#icon#', Handler.yaml_config['app']['app_icon'])
        if '#alter_app_name#' in info["json"]:
            info["json"] = info["json"].replace('#alter_app_name#', Handler.yaml_config['app']['alter_app_name'])
        if '#copy_app_name#' in info["json"]:
            info["json"] = info["json"].replace('#copy_app_name#', Handler.yaml_config['app']['copy_app_name'])
    headers = {}
    headers['Authorization'] = login['tokenType'] + ' ' + login['accessToken']
    # info 取出来是字典，转化为字符串
    all_data = json.dumps(info)
    # 字符串替换
    info = Handler.replace_data(all_data)
    print(info)
    # 字符串转化成字典
    info = json.loads(info)


    if info['method'] == 'get':
        res = requests.request(method=info["method"],
                               url=Handler.yaml_config['host'] + info['url'],
                               headers=headers)
    else:
        res = requests.request(method=info["method"],
                               url=Handler.yaml_config['host'] + info['url'],
                               headers=headers,
                               json=json.loads(info["json"]))
    res_body = res.json()
    print(res_body)
    # assert res.json()['code'] == info['expected']
    try:
        assert res_body['code'] ==  info['expected']
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        # excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('app',str(res_body),row=int(info['case_id']) + 1,column=8)
        if res_body['code'] == info['expected']:
            excel.write('app','True',row=int(info['case_id']) + 1,column=7)
        else:
            excel.write('app', 'False', row=int(info['case_id']) + 1, column=7)
    # 设置Handler对应的属性
    if info['extractor']:
        extrators = json.loads(info['extractor'])
        for prop,jsonpath_exp in extrators.items():
            # value = 'id'
            value = jsonpath(res.json(),jsonpath_exp)[0]
            # setattr(Handler,"laon_token","sadsadsfdgt")
            setattr(Handler,prop,value)


