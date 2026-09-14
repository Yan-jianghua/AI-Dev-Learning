import copy
# a = [11,22]
# b = [22,33]
# c = [a,b]
# d = c
# g = [a,b]
# e = copy.deepcopy(c)
# f = copy.copy(c)
# print("c = [a,b]",id(c))
# print("d = c:",id(d))
# print("e = copy.deepcopy(c)",id(e))
# print("f = copy.copy(c)",id(f))
# print("g = [a,b]",id(g))
# print("g[0]",id(g[0]))
# print("c[0]",id(c[0][0]))
# print("deepcopy",id(e[0]))
# print("copy",id(f[0][0]))

a = [1,2]
b = [3,4]
c = [5,6]
d = [7,8]

e = [a,b]
f = [c,d]

g = [e,f]

h = [g]
i = [e,f]
j = copy.deepcopy(g)
k = copy.copy(g)

print("""e = [a,b]
f = [c,d]

g = [e,f]

h = [g]
i = [e,f]
j = copy.deepcopy(g)
k = copy.copy(g)""")
print("g",id(g))
print("h",id(h))
print("i",id(i))
print("j",id(j))
print("k",id(k))
print(id(g[0][0]),id(a))
print(id(k[0][0]),id(a))