# 因为数据分组非常多，python更灵活

# 登陆成功的测试数据
success = [('looker53@sina.com', 'admin123456','yuze'),
           ('13925210746@163.com', 'admin123456','wagyu')]

# 用户名为空，密码为空
without_username_pwd = [('', '', ['账号不能为空', '密码不能为空'])]

# 用户名为空
without_username = [('','ab','账号不能为空'),
                    ('as','','密码不能为空')]

# 密码为空
without_pwd = [('as','','密码不能为空')]
