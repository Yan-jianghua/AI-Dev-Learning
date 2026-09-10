#打开文件
#open(name,mode,encoding)
#name:打开的文件名  mode:设置打开文件的模式（只读,写入，追加）   encoding:编码的格式推荐（UTF-8）
# | mode  | 含义    | 文件不存在时 | 特点         |
# | ----- | -----  | ------     | ---------- |
# | `"r"` | 读取    | 报错     | 只能读        |
# | `"w"` | 写入    | 创建     | **会清空原内容** |
# | `"a"` | 追加    | 创建     | 在末尾继续写     |
# | `"x"` | 创建    | 创建     | 文件已存在会报错   |
# | `"b"` | 二进制模式 | —      | 一般和其他模式组合  |
# | `"t"` | 文本模式  | —      | 默认模式       |

with open("C:/Users/y'j'h/Desktop/学习资料.txt",mode="rb") as f:
#读文件
#read()       → 全部内容 → 字符串
# readline()   → 一行内容 → 字符串
# readlines()  → 多行内容 → 列表 每一行为列表中的一个元素
# .seek(0)   把读取位置移动到开头
    print(f.read())
    f.seek(0)
    print(f.readlines())
#关闭文件
    f.close()
