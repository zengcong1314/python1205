import random
import time


def gen_class_name():
    """随机生成课程名称，字母，生成10位长度的字母。
    aacdeyualp"""
    name = ''
    for i in range(10):
        letter = random.choice('abcdefghijklmnopqrstuvwxyz')
        name += letter
    return name + str(int(time.time()))