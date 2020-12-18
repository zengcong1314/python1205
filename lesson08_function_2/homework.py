#1
def calculate(a,b):
    info = int(input("请选择【1】加 【2】减【3】乘 【4】除："))
    if info == 1:
        result = a + b
    elif info == 2:
        result = a - b
    elif info ==3:
        result = a * b
    elif info == 4:
        result = a / b
    else:
        print("输入有误，请重新输入！")
        return 0
    print(result)

calculate(10,40)
#2
def count_num():
    count = 0
    sum = 0
    while count < 10:
        name = input("请输入你的姓名：")
        age = int(input("请输入你的年龄："))
        if 15 <= age <=22:
            sum +=1
            print(sum)
            print("{}可以加入足球队".format(name))
        count += 1
    print("满足条件得总人数为：",sum)
count_num()

#3
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

def list_to_dict(cases):
    keys = cases[0]
    datas = cases[1:6]
    result1=[]
    for case in datas:
        adict = {}
        for idx,data in enumerate(case):
            # print(idx,data)
            adict[keys[idx]] = data
        result1.append(adict)
        #res1.append("\n")
    print(result1)
list_to_dict(cases)

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

fetch_data(res1)


