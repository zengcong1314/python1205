"""字符串的格式化"""
name = "李东霞"
money = 1000000
money_chinese = "一千万"

ticket = """
今收到  {} 
交来    {}
人民币  {}
""".format(name,money,money_chinese)
print(ticket)
