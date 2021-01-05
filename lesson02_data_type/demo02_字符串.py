#字符串表示：两个引号中间的数据
#单引号和双引号，三个引号
username = "zc"
username = """zc"""
username = 'zc'

#三个引号：可以表示多行字符串
last_name = "wang" \
            "h"
print(last_name)

last_name = "wang\nh"
print(last_name)

last_name = "wang\th"
print(last_name)

last_name = """wang
h
zxcsd"""
print(last_name)

#注释：三引号，字符串：三个引号
import keyword
print(keyword.kwlist)