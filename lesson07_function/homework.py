
def get_content(lst):
    if len(lst) > 2:
        lst = lst[0:2]
        return lst
    else:
        return lst

print(get_content([2,3,4,5,6]))

def remove_element(m_list):
    a = []
    for name in m_list:
        if name not in a:
            a.append(name)
    print(a)
m_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
remove_element(m_list)


def func_name(height, weight):
    BMI = weight/height**2
    if BMI < 18.5:
        print("过轻")
    elif  18.5 <= BMI <= 25:
        print("正常")
    elif 25 < BMI <= 28:
        print("过重")
    elif 28 < BMI <=32:
        print("肥胖")
    else:
        print("严重肥胖")
        return  BMI
func_name(1.72,100)
