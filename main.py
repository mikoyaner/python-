import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getProfiles
import random
d ={1:'注册人数更新', 2:'注 册 人 数 更 新', 3:'title自动换一下以免反垃圾邮件系统识别',4:'Registration Reminder',5:'更新注册人数',6:'提 醒 一下注册人数'}
# Press the green button in the gutter to run the script.
mail_user=input("请输入发件QQ邮箱地址：")
mail_pass=input("请输入发件邮箱密码，此为邮箱授权客户端密码，不是登录密码：")
receivers=input("请输入收件邮箱地址,此邮箱不能为腾讯下属的邮箱，会被识别为垃圾邮件：")
# mail_user='20122306007@m.scnu.edu.cn'
# mail_pass='bOOK110110'
sender=mail_user
# receivers=["amamylomm-7737@yopmail.com", "ufo.22@163.com"]
num1=0
x=10
while x>0:
    num = getProfiles.getpro()
    print(num)#调试程序
    if num1+200<num:
        num1=num
        print("现在的注册人数为"+str(num))
        try:
            smtp_obj=smtplib.SMTP_SSL("smtp.qq.com",465)
            smtp_obj.login(mail_user, mail_pass)
            message = MIMEText("现在的注册人数为"+str(num)+'，每增加200个人提醒一次，访问间隔为15分钟', 'plain', 'utf-8')
            message['From'] = Header(mail_user, 'utf-8')
            message['To'] = Header(receivers,'utf-8')
            rand=random.randint(1, 6)
            subject=d[rand]
            message['Subject'] = Header(subject, 'utf-8')
            smtp_obj.sendmail(sender, receivers, message.as_string())
            print('邮件发送成功!')
        except smtplib.SMTPException:
            print(smtplib.SMTPException)
            print("Error: 无法发送邮件")
            time.sleep(10)
            break
        # smtp_obj.sendmail(sender, "chmingxu@gmail.com", message.as_string())
        time.sleep(10)
    else:
        time.sleep(600)
        continue


