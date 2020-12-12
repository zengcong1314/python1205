a = ["zc",18]
#print(a.append("yu")) 操作指令，执行指令得到的结果，由函数返回值决定
b = a.append("yu") #这个操作是改变a的值，添加新的内容，具体返回什么，不清楚
print(b) #打印函数返回值
a.append("yu")
print(a)