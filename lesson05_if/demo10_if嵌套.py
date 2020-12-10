"""
if 嵌套，俄罗斯套娃
"""

age = 19
driver = False
work_hour = 10
if age > 18:
    print("我可以喝饮料")
    if driver:
        print("不能喝酒")
    else:
        if work_hour > 10:
            print("最好不好喝")
        elif 10 >= work_hour > 6:
            print("可以喝酒")
        else:
            print("没赚够钱，买不起酒")
else:
    print("未成年")

#if的后面bool
if not ["a"]:
    print("hello")
else:
    print("world")

#我们的for，while容易晕
#预习