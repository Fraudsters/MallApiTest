import unittest
import unittestreport
from common.handle_path import CASES_DIR,REPORT_DIR

suit=unittest.defaultTestLoader.discover(CASES_DIR)
runer=unittestreport.TestRunner(suit,filename="report.html",report_dir=REPORT_DIR,tester="zombie",desc="mall测试报告",templates=1)
runer.run()