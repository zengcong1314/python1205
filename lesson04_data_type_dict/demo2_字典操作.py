#不可变类型可以hash
#可变类型不可以hash

#可变类型
#增删改查
#key-value键值对

movies = {"favor":"画皮"
          }
#添加元素，insert
movies["new_key"] = "大话西游"
print(movies)
#删除
# movies.pop("favor")
# print(movies)

#修改 ，已经存在的key
#修改与添加的语法是一样的
#key之前没有这个key，就是添加，有这个key，就是修改
movies["new_key"] = "小花"
print(movies)

#获取所有的key
print(movies.keys())
#获取所有的values
print(movies.values())

#同时获取key,value
print(movies.items())

a = {1:"周末",2:"周末"}
print(a[2])
