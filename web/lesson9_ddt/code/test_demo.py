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
    print(info)