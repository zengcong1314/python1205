#多个值
songs = ["千里之外","那一夜","惊雷"]
#添加一个元素：变量名.append("新增的元素")
songs.append("课代表")
print(songs)

#一次添加多个元素，列表合并
songs.extend(['歌1','歌2'])
print(songs)

#可以选择添加的位置，insert
songs.insert(1,"曾聪最善良")
print(songs)

#删除操作
#清空列表当中的元素
# songs.clear()
# print(songs)
#一个个删除 remove，根据值删除
songs.remove("千里之外")
print(songs)

#根据索引删除
songs.pop(0)
print(songs)

#del
del songs[0]
print(songs)

#修改
#修改索引为0的元素
songs[0] = 1
print(songs)

#查，索引，切片
print(songs.count("课代表"))
#获取索引
# 字符串中find与index区别：find找不到索引返回-1，index找不到报错
print(songs.index("课代表"))

#排序
songs = [3,6,4,8]
songs.sort()
print(songs)
#反序
songs.reverse()
print(songs)