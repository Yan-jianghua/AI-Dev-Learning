#类型注解用于明确标识变量，函数参数和返回值的数据类型，从而使代码更清晰安全更容易维护

a : int = 698
score : float =122.2
hobby : str = "Hello"

names : list[str]  = ["a","b","c"]
name :list = [1,2,"hello"]
name2 : list[str|int] = [1,2,"hello","python"]
import math
def circle_area_len(r:float)-> float | int:
    return math.pi*r**2
