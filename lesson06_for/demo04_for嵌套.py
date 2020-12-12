#for 嵌套

cases = [
    ["http://example.com/login","get","yuz"],
    ["http://example.com/register","put","yw"],
    ["http://example.com/info","delete","wen"],
    ["http://example.com/project","options","achool"],
    ["http://example.com/interface","head","orange"],
]
#调试手段:print
#debug:pycharm 先让代码走到你想要的位置,左边打红点,红点表示:想让代码在这里暂停,红点叫断点
#python 代码从上到下
#Step Over F8:往下走一步,单步调试
#Step Into F7:进入某个函数
for case in cases:
    print("case:",case)
    for data in case:
        print("data:",data)

