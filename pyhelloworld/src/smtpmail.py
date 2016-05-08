#-*-coding:utf-8 -*-
'''
Created on 2016年5月8日

@author: liu
'''

import smtplib
from email.mime.text import MIMEText
from email.Header import Header

#第三方 SMTP 服务
mail_host = "smtp.douins.com" #设置服务器
mail_user = "yanchao.liu@douins.com"     #用户名
mail_pass = "ycliu@0912"      #口令

sender = "yanchao.liu@douins.com"
receivers = ['ycliu912@qq.com','ycliu912@126.com','yanchao.liu@douins.com'] #接受邮件

message = MIMEText('Python 邮件发送测试...','plain','utf-8')
message['From'] = Header("ycliu912",'utf-8')
message['To'] = Header("测试",'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error:无法发送邮件"


