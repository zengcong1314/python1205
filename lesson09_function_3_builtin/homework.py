#写出你接触过的内置函数，并说明他们的作用。
# min:最小值
# max:最大值
# sum:求和
# print:输出
# input:输入
# type:查看数据类型
# id:生成数据
# len:获取数据的长度（元素总数）
# int\float\bool\str\list\tuple\dict\set:代表对应的数据类型
# eval:
# 1、取出字符串中的内容，
# 2、将字符串str当成有效的表达式来求值并返回计算结果
# zip
# 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同


# ####编写如下程序有以下数据来自于一个嵌套字典的列表（可自定义这个列表），例如：
# person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,
# {"name":"cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"}
# ]
# 创建一个txt文本文件，来添加数据
# yuze,17,男,假正经, I am yours
# cainiao,18,女,看书,Lemon is best!

person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,
{"name":"cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"}
]
#取值，给我一个数据（输入），输出另一个数据
#get_string_from_list(lst):return ""
#一个函数对应的有某个功能，有参数与返回值，参数是输入的数据，输出是返回值
#把值写入文件,open(): write_file(person_info,file_name):return 文件
#函数是干什么用的？  ==》 函数的名称
# 输入
# 输出
def get_string_from_list(lst):
    """把list转化为字符串"""
    new_str = ""
    for line in lst:
        #line ={"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,
    # {"name":"cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"}
        # 获取字典所有的值
        for value in line.values():
            new_str += str(value) + ","
            #print(new_str)
        new_str = new_str.strip(",")
        new_str += "\n"
        print(new_str)
    return new_str

def write_file(person_info,file_name):
    f = open(file_name,'w',encoding="UTF-8")
    f.write(person_info)
    f.close()
    return file_name

new_str = get_string_from_list(person_info)
write_file(new_str,"person_info.txt")

#第二种方法
def get_string_from_list(lst):
    lines = ''
    for person in person_info:
        line = []
        for e in person.values():
            line.append(str(e))
        line_str = ','.join(line) + '\n'
        lines += line_str
    return lines

lst = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,
{"name":"cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"}
]
get_string_from_list(lst)
#第三种方法
for i in range (0,len(person_info)):
    data = list(person_info[i].values())
    #print(data)
    list2 = [str(i) for i in data]
    #print(list2)
    list3 = ",".join(list2)
    #print(list3)
    f = open("zc.txt",mode="a",encoding="UTF-8")
    f.write(list3)
    f.write("\n")
    f.close()

# 编写如下程序
# 有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
# [{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]

# 把txt里面的两行内容，read(file_name):return str,[]
# 转化为字典
def convent_to_dict(line):
    infos = line.split('@')
    info_dict = {}
    for info in infos:
        info_list = info.split(':')
        info_dict[info_list[0]] = info_list[1]
    return info_dict

f = open("demo.txt",mode="r",encoding="UTF-8")
lines = f.readlines()

new_lines = []
for line in lines:
    new = convent_to_dict(line.strip())
    new_lines.append(new)
print(new_lines)

#第二种方法
f = open("demo.txt",mode="r",encoding="UTF-8")
a = f.readlines()
print(a)
result = []
for i in a:
    sub_data = {}
    b = i.split('@')
    for j in b:
        c = j.split(':')
        c[1] = c[1].strip("\n")
        sub_data[c[0]] = c[1]
    result.append(sub_data)
print(result)


