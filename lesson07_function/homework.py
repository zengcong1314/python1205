#编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
#提示：参数为列表的变量 lst
def get_content(lst):
    if len(lst) > 2:
        lst = lst[0:2]
        return lst
    else:
        return lst

print(get_content([2,3,4,5,6]))

#定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
def remove_element(m_list):
    print (list(set(m_list)))
m_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
remove_element(m_list)

def remove_element(m_list):
    new_list = []
    for name in m_list:
        if name not in new_list:
            new_list.append(name)
    return new_list
m_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
print(remove_element(m_list))


def func_name(height, weight):
    BMI = weight/height**2
    if BMI < 18.5:
        return ("过轻")
    elif  18.5 <= BMI <= 25:
        return("正常")
    elif 25 < BMI <= 28:
        return("过重")
    elif 28 < BMI <=32:
        return("肥胖")
    else:
        return("严重肥胖")
res = func_name(1.72,100)
print(res)
