# 1.定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积＝底*高/2）。
def triangle_area(s,h):
    return s*h/2
s = float(input("请输入三角形的底:"))
h = float(input("请输入三角形的高:"))
print(f"三角形的面积为{triangle_area(s,h)}")
# 2，定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
def count_vowels(world):
    x = 0
    for i in world:
        if i == "a" or i == "e" or i == "i" or i == "u" or i == "o"or i == "A" or i == "E" or i == "I" or i == "U":
            x += 1
    return x
world = input("请输入一串英文字符:")
print("字符串中所含原因个数为:",count_vowels(world))
# 3，定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
def calculation(performance):
    performance.sort()
    print(f"最低分为{performance[0]}，最高分为{performance[-1]},平均分为{round(sum(performance)/len(performance),1)}")
    return {"最低分为":performance[0],"最高分":performance[-1],"平均分":round(sum(performance)/len(performance),1)}
a = []
print("请依次输入班级学生成绩(结束请输入-1）:")
while True:
    score = float(input())
    if score == -1:
        break
    else:
        a.append(score)
calculation(a)