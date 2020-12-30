import threading
import time
from math import *


def powX(x, n, results, index):
    results[index] = pow(x, n)


def giaiThua(n, results, index):
    result = 1
    for i in range(1, n):
        result *= i
    results[index] = result


if __name__ == '__main__':
    x = 4
    n = 5
    results = [None] * 2
    start = time.time()
    t1 = threading.Thread(target=powX, args=(x, n, results, 0))
    t2 = threading.Thread(target=giaiThua, args=(n, results, 1))
    t = [t1, t2]
    for i in range(len(t)):
        t[i].start()
    end = time.time()
    print(f"Total time: {format((end - start) * 1000, '.3f')}ms")
    result = float(results[0] / results[1])
    print(f'Result F(x, n) = {result}')


