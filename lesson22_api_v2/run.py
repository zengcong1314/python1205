"""
项目入口，主程序
收集项目，运行用例，生产报告
"""
import pytest
#from lesson22_api_v2.config import path
import os
# pytest 收集用例
# 如何放到reports里面
# TODO：报告如何不被覆盖  + 时间戳
# reports/report.html
#report_file = os.path.join(path.reports_path,'report.html')
pytest.main(['--html=report.html','-s'])

# python run.py

