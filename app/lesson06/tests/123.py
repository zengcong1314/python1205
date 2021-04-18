s = ["a","b","c","d","e","f"]
print(s[1:4:2])

ss = list(set("jzzszyj")) # jzsy
ss.sort()
print(ss)

# word = 'asadsf'
# counts = {}
# counts[word] = count[word] +1
#
# word.count()

cases = [['case_id','case_title','url','data','expected'],
         [1,'用例1','www.baidu.com','001','OK'],
         [2,'用例1','www.baidu.com','002','OK'],
         [3,'用例1','www.baidu.com','003','OK'],
         [4,'用例1','www.baidu.com','004','OK'],
         [5,'用例1','www.baidu.com','005','OK']]

res1 = []
title = cases[0]
print("title为：{}".format(title))
for data in cases[1:]:
    dic = {}
    for i in range(len(title)):
        dic[title[i]] = data[i]
    if dic['case_id'] > 3:
        res1.append(dic)
print(res1)



def count_money():
    money = 10
    for i in range(7):
        money = (money + 10) * 2
    print("小明第一天早上出门的金额为：",money)
count_money()