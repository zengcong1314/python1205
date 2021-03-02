import os
test_time = []
with open("data.log") as f:
    for line in f.readlines():
        temp = line.strip("\n").split(",")
        print("temp:",temp)
        if temp[-1] == str(0):
            test_time.append(int(temp[-2]))
        print(test_time)
if len(test_time) > 0:
    avg_time = sum(test_time) / len(test_time)
    max_time = max(test_time)
    min_time = min(test_time)
    print("最大的TestTime：",max_time,"最小的TestTime：",min_time,"平均TestTime：",round(avg_time,2))
    print("最大的TestTime{},最小的TestTime{},平均TestTime{}".format(max_time,min_time,round(avg_time,2)))
    # content = f.read()
    # print(content)