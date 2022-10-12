#读取excel测试用例数据
import openpyxl
class HandleExcel():
    def __init__(self,file_name,sheet_name):
        self.filename=file_name
        self.sheetname=sheet_name

    def read_data(self):
        """读取excel数据"""
        workbook=openpyxl.load_workbook(self.filename)
        sheet=workbook[self.sheetname]
        res=list(sheet.rows)
        #获取第一行标题头
        title=[i.value for i in res[0]]

        #获取其他用例数据
        cases=[]
        for item in res[1:]:
            data=[i.value for i in item ]
            dic=dict(zip(title,data))
            cases.append(dic)
        return cases
    def write_data(self):
        #后续补充
        pass





