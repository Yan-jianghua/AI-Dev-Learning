#生成1-20的平方列表
s = []
for i in range(20):
    s.append((i+1)**2)
print(s)
# 从如下数字列表中提取所有偶数做成新的列表
num_list = [19,23,54,65,87,20,109,232,123,26,55,72]
num = []
for x in num_list:
    if x % 2 == 0:
        num.append(x)
print(num)