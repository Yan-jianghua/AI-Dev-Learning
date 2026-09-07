def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名{name}，年龄{age},性别:{gender},城市{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}
#1.位置参数    调用函数时的参数顺序与定义函数时参数顺序完全一致

stu = reg_stu("张三",22,"男","上海")
print(stu)
#2.关键字传参   奥迪哦用函数是以函数定义形参的名称作为关键字，以”键=值"的形式传递参数
stu1 = reg_stu(age=22,name="李四",city="邯郸",gender="女")
print(stu1)
#3.位置传参+关键字传参 -------> 位置参数在前关键字参数在后
stu3 = reg_stu("张三",22,city="上海",gender="女")
print(stu3)


#默认参数    用于在定义参数是为参数提供默认值，调用时可以不传递默认值的参数,默认参数必须在非默认参数后
def reg_stu2(name,age,city,gender="男"):
    print(f"注册成功,姓名{name}，年龄{age},性别:{gender},城市{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}



#不定长参数          不确定参数的数量
    #位置参数
def calc_data(*args):   #传递所有匹配的位置参数都会被args变量收集,这些参数会合并封装为一个元组，args是元组类型
    return sum(args)

def calc(*args,**kwargs):
    """
    根据传入的数据,计算数据的最大最小平均值
    :param args:
    :param kwargs:
        round: 保留的小数位个数
        print: 是否打印
    :return:
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data,1)
    if kwargs.get("print"):
        print(f"最小值为{min_data}，最大值为{max_data},平均值为{avg_data}")
calc(1,2,3,4,round = 2,print= True)

#参数的类型 数字 布尔 字符串 列表 元组 集合 字典 函数
