"""
for 元素 in 待处理数据集:
   循环体
else:
   循环结束执行
"""
name = input("请输入需要遍历的元素:")
for i in name:
    print(i)
# 练习计算100-500之间所有3的倍数的和

#range(end)  range(start,end)  range(start,end,step)
# 获取从start到end的数据，没有start默认从0开始，step为步长
#包括头不包括尾部
a = 0
for b in range(100,500):
    if b%3==0:
        a=b+a
print(a)

