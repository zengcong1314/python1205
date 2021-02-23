import pytest
import os
from interface_homework.config import path
from datetime import datetime
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
report_file_name = 'repoert' + ts + '.html'
report_dir = path.reports_path

report_file=os.path.join(report_dir,report_file_name)
print(report_file)
pytest.main(['--html={}'.format(report_file),'-s'])