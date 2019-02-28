# coding:utf-8
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")

def send_mail(new_report):#发送‘最新测试报告’邮件
    f = open(new_report,'rb')#打开最新测试报告，不懂的同学看这个链接：http://www.runoob.com/python/python-func-open.html
    mail_body = f.read()#把读取到的测试报告信息赋给mail_body
    f.close()
    #邮件信息初始化
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('自动化测试报告','utf-8')
    #设置发送邮件服务器、发送者、发送对象
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')#邮件smtp设置，可以到QQ邮箱的设置里找到对应smtp
    smtp.login('xuzhengyu@bldz.com','Aa12345679')#邮件账户和密码
    smtp.sendmail('xuzhengyu@bldz.com',['603595306@qq.com',],msg.as_string())#发送者、收信者，发送内容
    smtp.quit()
    print('邮件发送成功')

def new_report(report_path):#获取‘最新’测试报告
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(report_path +'\\'+fn))#把所有测试报告按时间排序
    file_new = os.path.join(report_path,lists[-1])#取最后一份
    print(file_new)
    return file_new

def all_case():#定义所有测试用例
    discover = unittest.defaultTestLoader.discover(case_path,#测试路径
                                                    pattern="login.py",#需要执行的测试用例
                                                    top_level_dir=None)
    

    print(discover)
    return discover

if __name__ == "__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")#获取当前时间
    report_name = report_path+'/'+now+'result.html'#测试报告命名
    fp = open(report_name, 'wb')#写入新测试报告并保存到该路径文件夹
    runner = HTMLTestRunner(
        stream=fp,
        title=u'整站主流程测试报告',
        description=u'用例执行情况:'
    )#记录执行用例后的报告
    runner.run(all_case())#开始执行
    fp.close()
    #发送测试报告
    new_report = new_report(report_path)#获取最新测试报告
    send_mail(new_report)#发送最新测试报告