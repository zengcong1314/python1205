"""正则表达式：用来使用某种规则匹配字符串的子串
YUze  wang 123456
regular expression:正则表达式
"""

import re
my_string = 'yuzewang123456'
pattern = 'yuze'
result = re.search(pattern=pattern,string=my_string)
# 匹配对象
print(result)
# 得到最终的结果，默认值为0
# 要得到的匹配到的字符串，一定要加group()
print(result.group())

 # print(my_string.find('wang'))

 # [abc] 表示中括号当中任选其一
my_string = 'yuzewcng123456'
pattern = 'w[abc]ng'
result = re.search(pattern=pattern,string=my_string)
print(result)
print(result.group())

# . 只能匹配任意的一个字符串，除了\n换行符以外
# []
my_string = '@yuzewcng123456'
pattern = 'yuz.'
result = re.search(pattern=pattern,string=my_string)
print(result)
print(result.group())

# {m,n}匹配 m-n ,最少 m 次，最多 n 次，默认使用贪婪模式,取消贪婪模式加？
my_string = '@yuzewcng123456'
pattern = '.{6,9}'
result = re.search(pattern=pattern,string=my_string)
print(result)
print(result.group())

# {m}匹配 m，超出长度 返回 None
my_string = '@yuzewcng123456'
# .匹配任意字符7次
pattern = '.{7}'
result = re.search(pattern=pattern,string=my_string)
print(result)
print(result.group())

#investor_phone#
my_string = '{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#"}'
# 1、第一种方式
"""pattern = '#.{14}#' """
# 2、第二种方式 ,贪婪模式
"""pattern = '#.{,}#' """ # 左边是0，右边是无限大，match='#investor_phone#' 贪婪模式，如果一行有2个变量就不行
# 3、第三种方式，* 表示匹配0次或多次,
# ?表示非贪婪模式
# .*？常用组合：尽可能少的匹配任意字符
pattern = '#.*#' # match = '#investor_phone#","pwd":"#investor_pwd#'
pattern = '#.*?#' # match = '#investor_phone#'
result = re.search(pattern=pattern,string=my_string)
print(result)


my_string = '{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#"}'
# ?在数字不清楚的地方表示非贪婪模式
# ?表示0次或1次
pattern = '#?' # match = '{'
result = re.search(pattern=pattern,string=my_string)
print('-------------#:' , result)

# \w :字母 匹配一个字母
my_string = '{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#"}'
pattern = '\w+'
result = re.search(pattern=pattern,string=my_string)
print(result)

# \d:数字 匹配一个数字
my_string = '{"mobile_phone":"#134investor_phone#","pwd":"#investor_pwd#"}'
pattern = '\d'
result = re.search(pattern=pattern,string=my_string)
print(result)

# + 匹配任意字符1次或者任意次
my_string = '{"mobile_phone":"#134investor_phone#","pwd":"#investor_pwd#"}'
pattern = '\d+' # '\d{2}'
result = re.search(pattern=pattern,string=my_string)
print(result)

# () 分组
my_string = '{"mobile_phone":"#134investor_phone#","pwd":"#investor_pwd#"}'
pattern = '#.*?#'
result = re.search(pattern=pattern,string=my_string)
print(result.group())

# search 是只匹配一次
# finditer 找多个匹配数据
class Data:
    investor_phone = '13788881111'
    investor_pwd = '123456'
my_string = '{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#"}'
pattern = '#(.*?)#'
results = re.finditer(pattern=pattern,string=my_string)
for result in results:
    print(result)
    old_data = result.group()
    # key = 'investor_phone'
    key = result.group(1)
    new_data = getattr(Data,key,'')
    my_string = my_string.replace(old_data,new_data)

print(my_string)
"""
my_string = '{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#"}'
pattern = '#(.*?)#'
result = re.search(pattern=pattern,string=my_string)
print(result.group())
# group(1)获取括号当中的内容
# group(0)获取整个匹配内容
# 有1个括号就有group(1)，有2个括号才有group(2)，有2个括号的情况很少。
print(result.group(1))
"""

