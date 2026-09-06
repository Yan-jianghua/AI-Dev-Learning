#将用户输入的10个数字，存储到一个列表中，并江列表中的数字进行排列，输出其中最小，最大值和平均值
s = []
print("请输入十个数字")
for i in range(10):
    s.append(int(input()))

s.sort()
print(f"最小值为：{s[0]}")
print(f"最大值为:{s[-1]}")
print(f"平均值未{sum(s)/10}")

