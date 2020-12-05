name = "yuze wang"

print(name.count('e'))

name = "雨泽雨泽 雨最善良"
print(name.count(" "))

#字符串拼接,join是更加优雅的一种拼接方式
#多个字符串一定要放到列表或者元组当中
new_name = " ".join(["正常","正常","最善良"])
print(new_name)

#字符串 +
print("雨泽" + " " + "雨泽" +" " + "最善良")

#replace替换字符串
name = "雨泽雨泽最善良"
#替换之后要重新赋值
#字符串为不可变类型
new_name = name.replace('雨泽','曾聪')
print(new_name)

#split 字符串切割
#是和join对应的
name = " 雨泽/雨泽/最善良 "
print(name.split("/"))

#strip
print(name.strip(" "))