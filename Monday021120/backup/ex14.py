import threading
import time
from datetime import datetime
import math


class vector:
    def __init__(self, x1=1, y1=2, x2=3, y2=4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calEuclidean(self, results, index):
        result = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        results[index] = result

    def calManhattan(self, results, index):
        result = math.fabs(self.x2 - self.x1) + math.fabs(self.y2 - self.y1)
        results[index] = result

    def calCosin(self, results, index):
        result = float(1 - ((self.x1 * self.x2 + self.y1 * self.y2)/(math.sqrt(self.x1**2 + self.y1**2) * math.sqrt(self.x2**2 + self.y2**2))))
        results[index] = result


def processVector(x1, y1, x2, y2):
    print('*' * 20, 'Calculator Euclidean/Manhattan/Cosin', '*' * 20)
    vectorCal = vector(x1, y1, x2, y2)

    print('-' * 20, 'Sequentially', '-' * 20)
    startS = time.time()
    equalResult = [None] * 3
    vectorCal.calEuclidean(equalResult, 0)
    vectorCal.calEuclidean(equalResult, 1)
    vectorCal.calEuclidean(equalResult, 2)
    endS = time.time()
    totalS = endS - startS
    print('Space between A(' + str(vectorCal.x1) + ', ' + str(vectorCal.y1) + ') and B(' + str(vectorCal.x2) + ', ' + str(vectorCal.y2) + '):')
    print(f'- Euclidean: {equalResult[0]}')
    print(f'- Manhattan: {equalResult[1]}')
    print(f'- Cosin: {equalResult[2]}')
    time.sleep(0.5)

    print('-' * 20, 'Parallel', '-' * 20)
    startP = time.time()
    results = [None] * 3
    t1 = threading.Thread(target=vectorCal.calEuclidean, args=(results, 0))
    t2 = threading.Thread(target=vectorCal.calManhattan, args=(results, 1))
    t3 = threading.Thread(target=vectorCal.calCosin, args=(results, 2))
    t = [t1, t2, t3]

    print('-' * 10 + 'Detail thread open/end time' + '-' * 10)
    for i in range(len(t)):
        print(f"\t- Thread {i + 1} start in {datetime.now().strftime('%H:%M:%S.%f')}")
        t[i].start()

    for i in range(len(t)):
        t[i].join()
        print(f"\t- Thread {i + 1} end in {datetime.now().strftime('%H:%M:%S.%f')}")

    endP = time.time()
    totalP = endP - startP
    print(f'Total time parallel: ', format(totalP, '.10f'))

    print('Space between A(' + str(vectorCal.x1) + ', ' + str(vectorCal.y1) + ') and B(' + str(vectorCal.x2) + ', ' + str(vectorCal.y2) + '):')
    print(f'- Euclidean: {equalResult[0]}')
    print(f'- Manhattan: {equalResult[1]}')
    print(f'- Cosin: {equalResult[2]}')

    print('-' * 50)
    time.sleep(0.5)
    print('=' * 3 + '> Equal quality time: Sequentially ' + (
        '<' if totalS < totalP else '>') + ' Parallel ' + '<' + '=' * 3)


if __name__ == '__main__':
    print('-'*10 + 'Input value vector', '-'*10)
    x1 = float(input('Enter x1: '))
    y1 = float(input('Enter y1: '))
    x2 = float(input('Enter x2: '))
    y2 = float(input('Enter y2: '))
    processVector(x1, y1, x2, y2)
