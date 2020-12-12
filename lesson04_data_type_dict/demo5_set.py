#set 集合
# 和字典 {}
a = {1,3,6}
print(a)

#空集合：{}
a = set()
print(type(a))

#集合：不能有重复元素
#作用：去重
a = {1,11,1,1,2,3,4,4,4,6,6}
print(a)

cases = [4,7,8,4,5,3,4]
print(list(set(cases)))
#集合无序
#print(a[2])不能通过索引、key值获取
