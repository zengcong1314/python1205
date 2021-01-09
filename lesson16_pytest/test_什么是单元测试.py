import logging
import pytest



def add(a,b):
    """开发人员写的函数"""
    return a + b

@pytest.mark.smoke
def test_add():
    """封装起来的测试过程，叫做自动化测试用例
    test_开头的函数"""
    res = add(3,4)
    expected = 9
    if res == expected:
        print("测试用例通过")
    else:
        print("测试用例不通过")
# 不用if,用断言
def test_add2():
    """封装起来的测试过程，叫做自动化测试用例
    test_开头的函数"""
    res = add(3,4)
    expected = 9
    assert res == expected
    # 断言
    # 预期结果与实际结果比对，如果assert通过，程序正常执行。
    # assert不通过，会报错，AssertionError
    # try:
    #     assert expected == res
    # except AssertionError as e:
    #     logging.error("断言失败",e)
def test_minus():
    print("第二个用例有没有执行")
    assert 3 -2 == -1
if __name__ == '__main__':
    test_add2()
    test_minus()