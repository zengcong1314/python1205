# 针对多个值的运算
# {"token":"fdssfdgffhh"}
res = '{"token":"fdssfdgffhh"}'
print(type(res))
print("token" in res)
print("fdss" in res)

# 列表
dalao = ["clista","YW","haha"]
print("小脾气" in dalao)

dalao.append("小脾气")
print("小脾气" in dalao)

#字典
dalao = {"1":"clista","2":"学生","3":"T6"}
#不在里面，必须经过 key
#字典的 in 指的是key，不是value
print("clista" in dalao)
print("1" in dalao)