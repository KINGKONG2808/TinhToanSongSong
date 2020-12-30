import threading
import time
from math import *


def calFirst(x, results, index):
    results[index] = 2017


def calculatorS(x, i, n, results, index):
    result = 0
    for i in range(i, n):
        result += pow(x, n)
    results[index] = result


if __name__ == '__main__':
    x = 2
    n = 5
    results = [None] * 3
    start = time.time()
    t1 = threading.Thread(target=calFirst, args=(x, results, 0))
    t2 = threading.Thread(target=calculatorS, args=(x, 1, int(n / 2), results, 1))
    t3 = threading.Thread(target=calculatorS, args=(x, int(n / 2) + 1, n, results, 2))
    t = [t1, t2, t3]
    for i in range(len(t)):
        t[i].start()
    end = time.time()
    print(f"Total time: {format((end - start) * 1000, '.3f')}ms")
    fx = results[0] + results[1] + results[2]
    print(f'Result F(x, n) = {fx}')
