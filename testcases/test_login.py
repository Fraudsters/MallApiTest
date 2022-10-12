import os
import unittest
from unittestreport import ddt,list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR

@ddt
class TestLogin(unittest.TestCase):
    excel=HandleExcel(os.path.join(DATA_DIR,"cases.xlsx"),"login")
    cases=excel.read_data()
    pass
    @list_data(cases)
    def test_login(self,items):
        pass

    #1、准备用例数据
