import json
import uuid

from jsonpath import jsonpath
import requests
from middleware.handler import Handler
import pytest
prop_values = []
key_values = []

data = Handler.excel.read_dict('Data')

@pytest.mark.parametrize("info",data)
def test_data_screen(info,login,add_app):
    if info["json"]:
        if info["json"].find('#prop'):
            cun = info["json"].count('#prop')
            for i in range(20):
                format_index = str(i + 1)
                if len(prop_values) <= i:
                    val = str(uuid.uuid4())
                    prop_values.append(val)
                else:
                    val = prop_values[i]
                info["json"] = info["json"].replace('#prop' + format_index + '#', val)
    if info["json"]:
        if info["json"].find('#key'):
            for i in range(7):
                format_index = str(i + 1)
                if len(key_values) <= i:
                    val = str(uuid.uuid4())
                    key_values.append(val)
                else:
                    val = key_values[i]
                info["json"] = info["json"].replace('#key' + format_index + '#', val)
    if info["json"]:
        if "#titleProp#" in info["json"]:
            val3 = uuid.uuid4()
            info["json"] = info["json"].replace('#titleProp#', str(val3))

    if info["json"]:
        if "#app_id#" in info["json"]:
            print(str(add_app["app_id"]))
            info["json"] = info["json"].replace("#app_id#",str(add_app["app_id"]))
    if "#app_id#" in info["url"]:
        info["url"] = info["url"].replace("#app_id#", str(add_app["app_id"]))
    headers = {}
    headers['Authorization'] = login['tokenType'] + ' ' + login['accessToken']
    # info 取出来是字典，转化为字符串
    all_data = json.dumps(info)
    # 字符串替换
    info = Handler.replace_data(all_data)
    # print(info)
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
    #print(res_body)
    expected = json.loads(info['expected'])
    # assert res.json()['code'] == info['expected']
    for key,value in expected.items():
        # 实际结果的value 怎么获取
        try:
            jsonpath(res_body,key)[0] == value
        except AssertionError as e:
            Handler.logger.error("用例失败：{}".format(e))
            raise e
        finally:
            # excel = ExcelHandler(excel_file)
            excel = Handler.excel
            excel.write('Data',str(res_body),row=int(info['case_id']) + 1,column=8)
            if jsonpath(res_body,key)[0] == value:
                excel.write('Data','True',row=int(info['case_id']) + 1,column=7)
            else:
                excel.write('Data', 'False', row=int(info['case_id']) + 1, column=7)
    # 设置Handler对应的属性
    if info['extractor']:
        extrators = json.loads(info['extractor'])
        for prop,jsonpath_exp in extrators.items():
            # value = 'id'
            value = jsonpath(res.json(),jsonpath_exp)[0]
            # setattr(Handler,"laon_token","sadsadsfdgt")
            setattr(Handler,prop,value)



