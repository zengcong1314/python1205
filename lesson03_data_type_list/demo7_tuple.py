#元组是用()表示

a = (1,2)
print(a)
print(type(a))
print(len(a))
#元组如果是空的
a = ()
print(a)
print(type(a))
print(len(a))

#如果表示1个元素的元组：
#TODO：一定要在元素后加上一个逗号，不然的话，元组不生效
a = ("星河",1,2,3)
print(a)
print(type(a))
print(len(a))

#元组是不可变类型，只能查
print(a[0])
print(a[1:3])
print(a.index("星河"))
print(a.count("星河"))