#合并两个列表中的元素并去除重复元素
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
for j in num_list2:
    num_list1.append(j)
print(num_list1)
num_list3 = []
for x in num_list1:
    if x in num_list3:
        continue
    else:
        num_list3.append(x)
print(num_list3)