import pytest

#夹具：函数
@pytest.fixture(scope='function',autouse=True)
def function_before():
    """用例前置条件"""
    print("测试用例执行前")
    yield "hello" # 为啥不用return，函数遇到return就终止了，后置就不能执行了，越到yield执行中间的，执行完成后，再执行后面的，
    print("测试用例执行之后") # yield生成器函数,hello是函数返回值，没有是返回None

