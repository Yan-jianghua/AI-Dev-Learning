#计算阶乘
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
n = int(input("请输入一个数字"))
factorial(n)
print(f"{n}的阶乘为{factorial(n)}")


# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def total_price(*args,discount_coupon,integral,freight):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量
    :param discount_coupon: 优惠券
    :param integral: 积分抵扣
    :param freight: 运费
    :return: 订单的总金额
    """
    price = [goods[1]*goods[2] for goods in args]
    if sum(price) > 5000:
        if discount_coupon <= sum(price):
            if integral <= sum(price)-discount_coupon:
                return sum(price)-discount_coupon-integral+freight
            else:
                return freight
        else:
            return freight
    else:
        return sum(price)+freight
b=[]
print("结束输入请在商品名输入-1")
while True:
    a = []
    a.append(input("请输入商品名"))
    if a[-1] =="-1":
        break
    a.append(float(input("请输入商品单价")))
    a.append(int(input("请输入商品的数量")))
    b.append(a)
discount_coupon = int(input("请输入优惠券金额:"))
integral = int(input("请输入你的积分数"))
freight = 3
print(total_price(*b,discount_coupon = discount_coupon,integral = integral,freight=freight))

