#open 打开文件
#文件路径，如果没有路径，在当前目录查找文件。
#得到文件
f = open("demo.txt",encoding="UTF-8")
#声明文件的编码格式，计算机存储的是二进制数据，字符串如果要存储成二进制，通过一定的规则，转化成某一段01的数据，规则叫做编码格式
#一般默认编码格式是美国的ASCII编码，美国标准编码格式
#读取文件数据
#print(f.read())

#readlines 把所有数据一行一行存在一个列表里面
# print(f.readlines())
# #只读取一行
# print(f.readline())
f.close()

#文件的写入
#打开文件的模式：r,w
f = open("demo1.txt",mode='w',encoding="UTF-8")
f.write("helloword")
f.close()

#文件的关闭

#还有其他的额外的用法
