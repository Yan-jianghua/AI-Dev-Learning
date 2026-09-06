student = (
    ("s001", "王琳", 85,78,95),
    ("s002", "赵四", 88,55, 65),
    ("s003", "李四", 78, 54, 55),
    ("s004", "李五", 88, 85, 75),
    ("s005", "李晚", 98, 54, 85),
    ("s006", "王五", 87, 78, 66),
    ("s007", "郭晚", 79, 65, 88),
    ("s009", "张嘉", 75, 85, 95),
    ("s0010", "刘晚", 82, 88, 75)
)
a = 0
c = []
d = []
e = []
for i in range(len(student)):
    b = 0
    for j in range(len(student[i])):
        if j==2 or j==3 or j==4:
            a=a+student[i][j]
            b=b+student[i][j]
        if j==2:
            c.append(student[i][j])
        if j==3:
            d.append(student[i][j])
        if j==4:
            e.append(student[i][j])
    print(f"{student[i][1]}的总分为{b},平均分为{b/(len(student[i])-2)}")
    if b/(len(student[i])-2) >= 80:
        print(f"平均分大于80大家鼓励")
c.sort()
d.sort()
e.sort()
print(f"语文最低分为{c[0]},最高分为{c[-1]},平均分为{sum(c)/len(c)}")
print(f"数学最低分为{d[0]},最高分为{d[-1]},平均分为{sum(d)/len(d)}")
print(f"英语最低分为{e[0]},最高分为{e[-1]},平均分为{sum(e)/len(e)}")



