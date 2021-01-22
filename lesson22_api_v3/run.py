"""
项目入口，主程序
收集项目，运行用例，生产报告
"""
import pytest
from config import path
import os
from datetime import datetime
# pytest 收集用例
# 如何放到reports里面
# TODO：报告如何不被覆盖  + 时间戳
# reports/report.html

# 获取现在的时间戳
ts = datetime
print(ts)
# 获取测试报告存储目录
# report_dir = path.reports_path
# # 拼接文件
# report_file = os.path.join(report_dir,'report.html')
# pytest.main(['--html={}'.format(report_file),'-s'])

# python run.py

