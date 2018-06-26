# print(sum(range(1, 10100000)))
#
# from functools import reduce
#
# print(reduce(lambda a, b: a + b, range(1, 101)))
#
# a = 0
# print(sum([b for b in range(1, 101)]))
# a = map(lambda x: sum(range(x+1)), list(range(1, 101000)))
# print(list(a))

import time

"""
定义简单的装饰器,用来输出程序运行的所用时间
"""


def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("run the func use : ", d_time)

    return decor


@timer  # printSth = timer(printSth) -> printSth = decor
def printSth(str, count):
    for i in range(count):
        print("%d hello,%s!" % (i, str))


printSth("world", 100)
