# #1
# def calculate(a,b):
#     info = int(input("请选择【1】加 【2】减【3】乘 【4】除："))
#     if info == 1:
#         result = a + b
#     elif info == 2:
#         result = a - b
#     elif info ==3:
#         result = a * b
#     elif info == 4:
#         result = a / b
#     else:
#         print("输入有误，请重新输入！")
#         return 0
#     print(result)
#
# calculate(10,40)
# #2
# def count_num():
#     count = 0
#     sum = 0
#     while count < 10:
#         gender = input("请输入你的性别：")
#         age = int(input("请输入你的年龄："))
#         if 15 <= age <= 22 and gender == "女":
#             sum +=1
#             print(sum)
#             print("{}可以加入足球队".format(gender))
#         count += 1
#     print("满足条件得总人数为：",sum)
# count_num()
#
# def join_team(age,gender):
#     if 15 <= age <= 22 and gender == "女":
#         return True
#     return False
#
# def main():
#     num = 0
#     for i in range(10):
#         age = input("请输入你的年龄：")
#         gender = input("请输入你的性别：")
#         if not age.isdigit():
#             print("输入不合法。")
#             continue
#         joined = join_team(int(age),gender)
#         if joined:
#             num += 1
#     print(num)

#3
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
#adict = {}
def list_to_dict(cases):
    title = cases[0]
    result1=[]
    for case in cases[1:]:
        adict = {}#字典是可变的，不能定义在外边，每次执行完成一行后，重新定义一个新的变量
        for idx,data in enumerate(case):#同时获取索引与值
            # print(idx,data)
            adict[title[idx]] = data
            print(adict)#为啥adict = {}放在最外层时debug调试打印不出值
        result1.append(adict)
        #res1.append("\n")
    return result1
res = list_to_dict(cases)
print(res)

def transform_zip(cases):
    if type(cases) != list:
        print("不是list")
        return
    new_cases = []
    title = cases[0]
    for i in cases[1:]:
        new_dict = dict(zip(title,i))
        new_cases.append(new_dict)
    return new_cases

res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]

def fetch_data(res1):
    res = []
    for i in range (0,5):
        if res1[i]["case_id"] > 3:
            res.append(res1[i])
    print(res)
b = filter(res1,3)
print(b)

def filter(res1,id):
    new_cases = []
    for c in res1:
        if c["case_id"] > id:
            new_cases.append(c)
        return new_cases

fetch_data(res1)


