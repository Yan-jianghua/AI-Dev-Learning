"""
格式1:
    class 类名:
        pass
格式2：
    class 类名：
        pass
格式3:
    class 类名(父类名):
        pass
python中所有的类都直接或间接继承自object
"""

class Father:
    def __init__(self):
        self.gender = "男"
    @staticmethod
    def walk():
        print("饭后走一走,活到99")
class Son(Father):
    pass
son = Son()
son.walk()