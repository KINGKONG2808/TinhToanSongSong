import threading
import time
from math import *


def calFx(x, n, results, index):
    results[index] = 2 * pow(x, 2) + n * x + n


if __name__ == '__main__':
    x = 2.5
    y = 5.5
    n = 4
    results = [None] * 3
    start = time.time()
    t1 = threading.Thread(target=calFx, args=(x, n, results, 0))
    t2 = threading.Thread(target=calFx, args=(y, n, results, 1))
    t3 = threading.Thread(target=calFx, args=(x + y, n, results, 2))
    t = [t1, t2, t3]
    for i in range(len(t)):
        t[i].start()
    end = time.time()
    print(f"Total time: {format((end - start) * 1000, '.3f')}ms")
    p = results[0] + results[1] - results[2]
    print(f'Result S = {p}')
