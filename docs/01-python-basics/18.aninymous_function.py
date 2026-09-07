#定义匿名函数   只能用于简单函数
#函数名 = lambda 参数列表 : 函数体
#匿名函数可以返回结果也可以不反回结果，不需要写retuen,表达式的运行结果就是要返回的结果


#按照字符长度排列
data_list = ["C++","C","Go","Java","JavaScript","Python"]
data_list.sort(key = lambda x : len(x))
print(data_list)