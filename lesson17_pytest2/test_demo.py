def test_demo():
    """当用例没有通过时，需要额外处理，日志处理
    测试用例不通过，抛出异常,才是用例执行失败"""
    try:
        print("try")
        assert 1 + 1 == 2
    except AssertionError as e: # 捕获异常
        print("测试用例正在执行",e)
        raise e  #抛出异常