class Student:
    def __init__(self , name:str , weight:float):
        self.name = name
        self.weight = weight
    def eat_food(self):
        self.weight +=2
    def __str__(self):
        return f'{self.name} {self.weight}'
    def run(self):
        self.weight -= 0.5
    def __del__(self):
        print(f"{self}被删除")
c1 = Student("小明",100)
print(c1)
c1.eat_food()
c1.run()
print(c1)