import threading
import time
from datetime import datetime
from math import *


class fx:
    def __init__(self, x=2):
        self.x = x

    def calculator(self):
        result = (pow(self.x, 2) + exp(fabs(self.x)) + pow(sin(self.x), 2))/(pow((pow(self.x, 2) + 1), 1/5))
        return result

    def getNumerator(self, results, index):
        result = pow(self.x, 2) + exp(fabs(self.x)) + pow(sin(self.x), 2)
        results[index] = result

    def getDenominator(self, results, index):
        result = pow((pow(self.x, 2) + 1), 1/5)
        results[index] = result


def process(x):
    print('*' * 20, 'Calculator F(x)', '*' * 20)
    fxCal = fx(x)

    print('-' * 20, 'Sequentially', '-' * 20)
    startS = time.time()
    resultS = fxCal.calculator()
    endS = time.time()
    totalS = endS - startS
    print(f"=> Result run by sequentially: {resultS} in {format(totalS, '.10f')}s")

    time.sleep(0.5)

    print('-' * 20, 'Parallel', '-' * 20)
    startP = time.time()
    results = [None] * 2
    t1 = threading.Thread(target=fxCal.getNumerator, args=(results, 0))
    t2 = threading.Thread(target=fxCal.getDenominator, args=(results, 1))
    t = [t1, t2]

    print('-' * 10 + 'Detail thread open/end time' + '-' * 10)
    for i in range(len(t)):
        print(f"\t- Thread {i + 1} start in {datetime.now().strftime('%H:%M:%S.%f')}")
        t[i].start()

    for i in range(len(t)):
        t[i].join()
        print(f"\t- Thread {i + 1} end in {datetime.now().strftime('%H:%M:%S.%f')}")

    resultParallel = results[0] / results[1]

    endP = time.time()
    totalP = endP - startP
    print(f'Total time parallel: ', format(totalP, '.10f'))

    print(f'=> Result parallel calculator: {resultParallel}')

    # print('-' * 50)
    # time.sleep(0.5)
    # print('=' * 3 + '> Equal quality time: Sequentially ' + (
    #     '<' if totalS < totalP else '>') + ' Parallel ' + '<' + '=' * 3)


if __name__ == '__main__':
    x = float(input('Enter x: '))
    process(x)
