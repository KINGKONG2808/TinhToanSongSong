import threading
import time
from math import *


def giaiThua(number, results, index):
    result = 1
    for i in range(1, number):
        result *= i
    results[index] = result


if __name__ == '__main__':
    a = 4
    b = 5
    results = [None] * 3
    start = time.time()
    t1 = threading.Thread(target=giaiThua, args=(a, results, 0))
    t2 = threading.Thread(target=giaiThua, args=(b, results, 1))
    t3 = threading.Thread(target=giaiThua, args=(a + b, results, 2))
    t = [t1, t2, t3]
    for i in range(len(t)):
        t[i].start()
    end = time.time()
    print(f"Total time: {format((end - start) * 1000, '.3f')}ms")
    result = float((results[0] + results[1]) / results[2])
    print(f'Result (a! + b!)/(a+b)! = {result}')


