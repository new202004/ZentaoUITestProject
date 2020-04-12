import os
import time
import unittest
import HTMLTestRunner

current_path = os.path.dirname(__file__)
report_path = os.path.join(current_path, 'report')
cases_path = os.path.join(current_path, 'test_cases')
html_path = os.path.join(report_path, 'report_%s.html' % time.strftime('%Y_%m_%d_%H_%M_%S'))

discover = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern='*_case.py',
                                               top_level_dir=cases_path)  # 初始路径,文件类型，顶级路径

main_suite = unittest.TestSuite()
main_suite.addTest(discover)

suite = unittest.TestSuite()
file = open(html_path, 'wb')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='禅道UI自动化测试项目', description='UI自动化测试完成，包含大部分')
html_runner.run(main_suite)