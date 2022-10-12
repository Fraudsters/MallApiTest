import os
import unittest

import requests
from unittestreport import ddt,list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf

@ddt
class TestLogin(unittest.TestCase):
    excel=HandleExcel(os.path.join(DATA_DIR,"cases.xlsx"),"login")
    cases=excel.read_data()
    base_url=conf.get("env","base_url")
    headers=eval(conf.get("env","headers"))

    pass
    @list_data(cases)
    def test_login(self,items):
        pass
        #准备测试用例数据
        url=self.base_url+items['url']
        method=items['method'].lower()
        para=eval(items['data'])
        expected=eval(items['expected'])

        reponse=requests.request(method,url,json=para,headers=self.headers)
        res=reponse.json()
        print(res)
    #1、准备用例数据
