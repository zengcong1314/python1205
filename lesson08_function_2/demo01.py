def add(a,b):
    c = a + b
    d = c * a
    e = d * b
    return d

add(3,4)# ==> 调用函数得到值是函数得返回值

print(add(3,4))

b = add(3,4)
print(b)