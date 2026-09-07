#组织好的可重复使用的，用来实现特定功能的
# def 函数名(参数列表):
#函数要写说明文档在函数开头注释，解释函数功能，参数，返回值 help(函数名)可查看函数的说明文档
import math

def circle_area(radius):
    """
    计算圆的面积
    :param radius:半径
    :return: 面积
    """
    return math.pi * radius**2
r = 1
circle_area(r)