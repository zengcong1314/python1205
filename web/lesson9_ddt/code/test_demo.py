import pytest

data = [(1,1,2),(3,2,4)]
# def test_add_1():
#     assert 1+1 == 2
#
# def test_add_2():
#     assert 3+2 ==5
@pytest.mark.parametrize('info',data)
def test_add(info):
    # (1,1,2),(3,2,4)
    assert info[0] + info[1] == info[2]

@pytest.mark.parametrize('param1,param2,expected',data)
def test_add(param1,param2,expected):
    # (1,1,2),(3,2,4)
    assert param1 + param2 == expected