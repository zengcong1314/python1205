#索引 index ，目录，通过一定的顺序更快捷的找到字符串当中的某个字符
#abc

#公式：字符串[索引]
#TODO：python获取索引是从0开始，不是1
#空格也算一个字符
name = "yuze wang"
print(name[1])
print(name[0])

name = """wang
poi
qaaa"""
print(name)
print(name[5])

#索引为负数，是从右边开始
name = "yuze wang"
print(name[-1])

#IndexError: string index out of range
#索引超出范围了怎么办
#print(name [100])

#获取字符串的长度
print(len(name))

name = "hello,'zc'"
print(name)

#列表和索引的区别
#列表数据 a = [1,3,4]
#索引的前面 “string”[]