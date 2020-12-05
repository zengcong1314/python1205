#切片：想获取多个字符的时候，你有把刀，去切这个字符串
name = "yuze wang"

#开始位置和结束位置
#公式：字符串[strat:end]
#切片顾头不顾腚，顾头不顾尾
print(name[1:3])
print(name[0:5])

#公式：字符串[strat:end：step]
#0,2,4
print(name[0:6:2])

#公式3：字符串[start:]
print(name[1:])
print(name[:6])
print(name[:])
#复制
name_copy = name[:]
print(name_copy)
#倒叙排序
print(name[::-1])
print(name[-1::-1])
name = "yuze wang"
#步长能不能为负数
print(name[-1:-3:-1])
print(name[-3:-1])

#取不到数据
print(name[-1:-3:1])
#-1往右边取数，步长往左边取数，所以python取不到数据
#总结：
#心法：
#第一步：end - start
#第二步：step
#步长两个计算保持符号一致
print(name[-1:0])  #1，1这里方向一样，为啥取不到值，-1是最后的字符，要想取到值，只能往左边
#步长正数往右边去，负数往左边去