#无序和有序
#字典是无序的
#列表、元组、字符串都是有序的

#能用索引获取的就是有序的
#不能用索引的就是无序的，key
#所有字典的操作都是通过key的

#可变和不可变
#可变：列表、字典  可以改变里面的“元素”
#不可变：字符串、元组、整形  不可以修改里面的元素

a = [1,2,("hello","word")]
# a[2]="orange"
# print(a)
print(a[2][0])
#a[2][0] = 'love'  不能修改元组内元素

b = (["hello","word"],("ming","ming"))
print(b[0])
# b[0] = True 不可以，报错TypeError: 'tuple' object does not support item assignment
# print(b)

b[0][0] = True
print(b)

# b[1][0] = True 不可以，报错
# print(b) TypeError: 'tuple' object does not support item assignment