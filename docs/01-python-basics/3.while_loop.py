# while 条件表达式:
#        循环语句1:
#        循环语句2:

# while 条件语句:
#     循环语句:
# else:(只执行一遍)
i=1
while i<10:
    print(i)
    i+=1
else:
    i-=1
    print("no")

# 练习 1-100的偶数的和
i=0
j=0
while i<=100:
    i+=1
    if i%2==0:
        j=j+i
print(j)