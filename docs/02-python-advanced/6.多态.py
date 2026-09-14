#同一个函数，接受不同的参数，有不同的效果
"""
  1,要有继承
  2，要有方法重写
  3，要有父类引用指向子类
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

class Dog(Animal):
    def speak(self):
        print("汪汪")

def make_noise(an:Animal):
    an.speak()

make_noise(Cat())
make_noise(Dog())