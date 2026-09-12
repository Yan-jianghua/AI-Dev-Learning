class Car:
    def __init__(self,color:str,model:str,year:int):
        self.color=color
        self.model=model
        self.year=year
c1 = Car("蓝色","特斯拉model Y",2026,)
print(c1.color)
print(c1.model)
print(c1.year)
