# while True:
#     print("我喜欢你")
# print("你够了！！！！")
times = 0
while True:
    if times <= 99:
        print("你不够坚持")
        continue #不再执行此轮循环，进入下一个循环
        print("谢谢你")
    else:
        print("我答应你，我也喜欢你")
        #强制退出循环
        break
    times += 1
    print("我喜欢你")


print("你够了！！！！")
