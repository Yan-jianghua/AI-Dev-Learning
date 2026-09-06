"""
  需求：根据输入的用户名密码执行登录操作，具体要求如下:
1.正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
2.输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
3.输入的用户名和密码不能为空！
4.登录成功：输出“登录成功，进入B站首页~"
5.登录失败：输出“用户名或密码错误，请重新输入！
"""
account1 = "admin"
account2 = "zhangsan"
account3 = "taoge"
password1 = "666888"
password2 = "123456"
password3 = "888666"
while True:
            account = input("请输入你的账号:")
            password = input("请输入你的密码")
            if (password == password1 and account == account1) or (password == password2 and account == account2) or (password == password3 and account == account3):
                 print("登录成功，进入B站首页~")
                 break
            else:
               print("账号或密码错误请重新输入")

# import random       random.randint(start,end)  生成start到end的随机数
""""
1.系统随机生成一个随机数
2.用户根据提示猜数字，并将所猜的数字输入系统
3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4.如果猜对，系统自动退出，游戏结束
"""
import random
x=random.randint(1,100)
while True:
       x1=int(input("请输入您猜测的数字:"))
       if x>x1:
        print("猜小了")
        continue
       elif x<x1:
        print("猜大了")
        continue
       else:
        print(f"数字为{x1}")
        break