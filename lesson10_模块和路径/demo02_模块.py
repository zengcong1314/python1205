"""
一个PY的文件就叫模块
包：包含__init__.py的文件夹就叫做包
模块和包有什么作用？
组织代码的。

按照功能分类存储，函数就会存到不同的模块当中
不同用途的模块又分别存到包里。

模块：内置模块和第三方模块。
如果我们想使用其他模块的代码，就需要导入。import
"""
#内置模块 用import
import time
# 调用 time 模块当中的time函数
print(time.time())
# 现在这个时间的时间戳

# 第三方模块的导入
# 路径从项目的根目录开始
# import lesson10_模块和路径.d01_open
# a = lesson10_模块和路径.d01_open.add(3,4)
# print(a)

#自己写的代码用from
from lesson10_模块和路径 import d01_open
a = d01_open.add(3,4)
print(a)

def add(a,b):
    return a - b

#直接导入函数
from lesson10_模块和路径.d01_open import add as module_add
b = module_add(3,4)
print(b)


#调用的是最后出现的那个
#在一个文件当中，如果出现同名的函数，之前的那个会被覆盖掉
#当导入的标识符出现同名，一定要把其中的一个取别名，以免混淆
c = add(3,4)
print(c)

print(d01_open.add(3,4))

#最后，导入所有
from lesson10_模块和路径.d01_open import *
add()

#import：内置模块导入，不能导入函数，只能导入模块
# from ....import .... 主要用在自定义模块导入
# from ....import ....既可以导入模块，还可以直接导入函数
# from ....import....as....重命名
# from ....import * ,强烈建议不要用

from time import time
time()

import time
time.time()


