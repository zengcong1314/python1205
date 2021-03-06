import json

import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('cases')
@pytest.mark.parametrize("info", data)
def test_add_cases(info,login,add_projects,add_interface):
    headers = {"Authorization":login["token"]}
    if "#case_name#" in info['json']:
        cases_name = Handler.generate_random_str(6)
        info['json'] = info['json'].replace('#case_name#',cases_name)
    if "#project_id#" in info['json']:
        project_id = add_projects['project_id']
        info['json'] = info['json'].replace('#project_id#',str(project_id))
    if '#interface_id#' in info['json']:
        interface_id = add_interface['interface_id']
        info['json'] = info['json'].replace('#interface_id#', str(interface_id))
    res = requests.request(method='POST',
                           url=Handler.yaml_config['host'] + info['url'],
                           headers=headers,
                           json=json.loads(info['json']))

    assert res.status_code == info['expected']