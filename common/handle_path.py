"""
此模块专门用例处理项目中的绝对路径
"""
import os
BASE_DIR=os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
LOG_DIR=os.path.join(BASE_DIR,"logs")
CONF_DIR=os.path.join(BASE_DIR,"conf")
DATA_DIR=os.path.join(BASE_DIR,"datas")
REPORT_DIR=os.path.join(BASE_DIR,"reports")
CASES_DIR=os.path.join(BASE_DIR,"testcases")


