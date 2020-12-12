cases = [
    {"url":"/login","method":"get"},
    {"url":"/register","method":"post"},
    {"url":"/project","method":"put"}
]

for case in cases:
    for k,v in case.items():
        print(k,v)