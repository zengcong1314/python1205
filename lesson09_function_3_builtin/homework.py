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

f = open("demo.txt",mode="r",encoding="UTF-8")
a = f.readlines()
print(a)
result = []
for i in a:
    sub_data = {}
    b = i.split('@')
    for j in b:
        c = j.split(':')
        c[1]=c[1].strip("\n")
        sub_data[c[0]]=c[1]
    result.append(sub_data)
print(result)




