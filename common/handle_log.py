#用于日志收集
import logging
def create_log(name="mylog",level="DEBUG",sh_level="DEBUG"):
    #创建日志收集器
    conf=logging.getLogger(name)
    #设置日志收集器收集日志级别
    conf.setLevel(level)

    #设置日志收集渠道

    #1、设置控制台日志输出
    sh=logging.StreamHandler()
    #2、设置控制台日志输出级别
    sh.setLevel(sh_level)
    conf.addHandler(sh)
