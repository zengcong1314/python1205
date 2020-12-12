# or and  not
#and 并且
#or 或者

data = 5 > 3
print(data)

door = 4 == 3
print(door)
#and，左边和右边必须同时为真，True，才能为真，否则就是False
print(data and door)

#or，左边和右边只要有一个为真，就为True
print(data or door)

# not 反面：杠精
print(not door)

print( 5 > 6 and 7 < 3 or "zc" == "旧梦")
#运算优先级 多个运算，先算哪个
#()括号提高优先级
