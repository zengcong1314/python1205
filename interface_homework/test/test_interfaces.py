import json

import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('interfaces')
@pytest.mark.parametrize("info", data)
def test_interfaces(info,login,add_projects):
    if "#token#" in info['headers']:
        info['headers'] = info['headers'].replace('#token#',login['token'])
    if "#interface_name#" in info['json']:
        interface_name = Handler.generate_random_str(6)
        info['json'] = info['json'].replace('#interface_name#',interface_name)
    if "*interface_name*" in info['json']:
        interface_name = Handler.user_config['user']['interface_name']
        info['json'] = info['json'].replace('*interface_name*',interface_name)
    if "#project_id#" in info['json']:
        project_id = add_projects['project_id']
        info['json'] = info['json'].replace('#project_id#',str(project_id))
    # no_project_id#
    if "#no_project_id#" in info["json"]:
        sql = 'select max(id) from tb_interfaces'
        result = Handler.db.query(sql)
        info['json'] = info['json'].replace('#project_id#', str( result['max(id)'] + 10))
    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'],
                           headers=json.loads(info['headers']),
                           json=json.loads(info['json']))
    assert res.status_code == info['expected']