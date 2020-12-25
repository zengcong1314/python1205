def add(a,b):
    if isinstance(a,int) and isinstance(b ,int):
        return a + b
    else:
        raise ValueError("数据类型不对")
print(add('3',4))
