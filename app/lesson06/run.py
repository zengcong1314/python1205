import pytest

# 执行 pytest 的指令
# 指令和在命令行输入 pytest --alluredir=report
# 入口文件
# run.py 和 pytest 命令行是等价的
pytest.main(['--alluredir=allure'])
