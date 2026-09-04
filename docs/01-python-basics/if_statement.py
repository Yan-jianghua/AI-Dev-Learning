#if语句
account_number="1223344"
password="yan060918"
account_number1=input("请输入你的账号：")
password1=input("请输入你的密码:")
r1=(account_number1=="1223344")
r2=(password1=="yan060918")
if r1:
    if r2:
        print("登录成功")
    else:
        print("密码错误")
else:
    print("账号不存在")

