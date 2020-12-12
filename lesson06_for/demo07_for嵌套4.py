keys = ["url","method"]
cases = [
    ["/register","get"],
    ["/register","post"],
    ["/project","put"],
]
# cases = [
#     {"url":"/login","method":"get"},
#     {"url":"/register","method":"post"},
#     {"url":"/project","method":"put"}
# ]
#列表转成字典
lst = []
for case in cases:
    adict = {}
    #同时获取列表的索引和值
    for idx, data in enumerate(case):
        print(idx,data)
        #adict["url"] = "login"
        #adict["method"] = "post"
        adict[keys[idx]] = data
    print(adict)
    lst.append(adict)
print(lst)


lst = ["a","b","c"]
for i in lst:
    print(i)

lst = ["a","b","c"]
for index,i in enumerate(lst):
    print(index,i)