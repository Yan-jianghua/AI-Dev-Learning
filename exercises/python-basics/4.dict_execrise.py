# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
# 通过控制台菜单与用户交互。具体功能如下：
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx，商品价格：xxx，商品数量：xxx”。
# 5.退出购物车
shop = {
    }
print(f"您的购物车中有{shop}")
print("添加商品请按    1      ")
print("修改购物车请按   2      ")
print("删除商品请按     3      ")
print("查询商品请按     4       ")
print("退出购物车请按   5        ")
while True:
    a = int(input("请输入您要进行的操作所对应编号:"))
    match a:
        case 1:
            goods_name = input("请输入你要添加的商品名称:")
            goods_num = int(input("请输入商品数量:"))
            if goods_name in shop:
                # 商品已存在，只累加数量（价格保持不变）
                shop[goods_name]["num"] = shop[goods_name]["num"] + goods_num
            else:
                goods_price = float(input("请输入商品价格:"))
                shop[goods_name] = {"price": goods_price, "num": goods_num}
            print(f"您的购物车中有{shop}")
        case 2:
            goods_name = input("请输入你要修改的商品名称:")
            if goods_name in shop:
                goods_price = float(input("请输入商品价格:"))
                goods_num = int(input("请输入商品数量:"))
                shop[goods_name] = {"price": goods_price, "num": goods_num}
                print(f"修改成功!您的购物车中有{shop}")
            else:
                print("该商品不存在,请先添加商品!")
        case 3:
            goods_name = input("请输入你要删除的商品名称:")
            if goods_name in shop:
                del shop[goods_name]
                print(f"删除成功!您的购物车中有{shop}")
            else:
                print("该商品不存在!")
        case 4:
            if shop:
                for goods_name, info in shop.items():
                    print(f"商品名称:{goods_name},商品价格:{info['price']},商品数量:{info['num']}")
            else:
                print("购物车为空!")
        case 5:
            print("已退出购物车,再见!")
            break
        case _:
            print("非法操作，请重新输入")
