import random
d ={1:'注册人数提醒', 2:'注 册 人 数 提 醒', 3:'title换一下以免反垃圾邮件系统识别',4:'Registration Reminder'}
x=10
hello=input("请输入参数")
while x>=0:
    a=random.randint(1, 4)
    strings=d[a]
    print(strings)
    print(hello)
    x=x-1