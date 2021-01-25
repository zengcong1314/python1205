import pytest

@pytest.fixture(autouse=True)
def connect():
    print("链接")
    return "大脸猫"

# 获取夹具的返回值，必须手动传入夹具，不能用autouse=True
def test_demo(connect):
    print("helloword")
    print(connect)