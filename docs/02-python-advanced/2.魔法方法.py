#__init__
#__str__ 当用print()函数 打印对象的时候 会自动调用该对象（所在类）的str魔法方法
#__del__ 当python文件执行结束或者手动del释放对象资源，会自动调用该函数
#定义汽车里类，默认属性黑色 number=3
class Car:
    def __init__(self, color:str, number:int):
        self.color = color
        self.number = number
    def __str__(self) -> str:
        return f'{self.color} {self.number}'

    def __del__(self):
        print(f'{self}对象被删除了')
c1 = Car('red', 3)
print(c1)
c2 = Car('blue', 4)
print(c2)
del c1
print('程序结束')