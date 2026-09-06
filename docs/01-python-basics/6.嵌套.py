#输出一个长为n宽为m的*矩阵
n = int(input("请输入矩形的长："))
m = int(input("请输入矩形的宽："))
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()
#打印九九乘法表
n = 1
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print(f"{j}*{i}={i*j}",end=" ")
    print()