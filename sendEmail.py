#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

#qq邮箱smtp服务器
host_server='smtp.qq.com'
#发件人邮箱
send_qq_mail='1103068881@qq.com'
#校验码
pwd = 'abcnhtepfxxdbaac'
#收件人邮箱
receiver=''

#邮件内容
content="登录接口测试报告，见附件"

title='自动发送的邮件'

#ssl登录
smtp = SMTP_SSL(host_server)
smtp.login(send_qq_mail,pwd)

#创建一个带附件的实例
msg=MIMEMultipart()
msg['From']=send_qq_mail
msg['To']=receiver
#邮件标题
msg['Subject']=Header(title,'utf-8')
#邮件正文内容
msg.attach(MIMEText(content,'plain','utf-8'))

#附件
att=MIMEApplication(open('''D:\\pythonworkspace\\untitled\\HTMLReport.html''','rb').read())
att.add_header('Content-Disposition','attachment',filename='report.html')
msg.attach(att)

#发送邮件
smtp.sendmail(send_qq_mail,receiver,msg.as_string())

#关闭
smtp.quit()
print('邮件发送成功')