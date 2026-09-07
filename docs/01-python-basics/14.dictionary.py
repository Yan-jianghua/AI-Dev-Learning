#dict
#dict{键盘:数据,"b":222,...}
#键不可重复，可修改 key必须是不可变类型（srt int float tuple）

#获取
dict1 = {0:90,2:"323"}
dict2 = {1:90,2:"323"}
print(dict1[0])
#修改
dict1[0] = 30
print(dict1[0])
print(dict1)
print(dict1.items())

#增
#字典名[key] = 值   key值不可重复重复会覆盖

#删
#字典名.pop(key)
#del 字典名[key]

#改
#字典名[key] = value

#查
#字典名[key]
#字典名.get(key)
#字典名.keys()     获取所有键
#字典名.values()   获取所有值
#字典名.items()  获取所有对