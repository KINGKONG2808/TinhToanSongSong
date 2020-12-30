import threading
import time
from datetime import datetime
import math


class vector:
    x = None
    y = None

    def __init__(self, x1=1, y1=2, x2=3, y2=4, x3=5, y3=6):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def getCenterPoint(self):
        vector.x = float((self.x1 + self.x2 + self.x3) / 3)
        vector.y = float((self.y1 + self.y2 + self.y3) / 3)

    def getCenterPointCopy(self, results, index):
        vector.getCenterPoint(self)
        results[index] = vector.x
        results[index+1] = vector.y

    def calEuclidean(self, results, index):
        result = math.sqrt((self.x1 - vector.x) ** 2 + (self.y1 - vector.y) ** 2) + math.sqrt(
            (self.x2 - vector.x) ** 2 + (self.y2 - vector.y) ** 2) + math.sqrt(
            (self.x3 - vector.x) ** 2 + (self.y3 - vector.y) ** 2)
        results[index] = result


def processVector(x1, y1, x2, y2, x3, y3):
    print('*' * 20, 'Calculator Euclidean/Manhattan/Cosin', '*' * 20)
    vectorCal = vector(x1, y1, x2, y2, x3, y3)

    print('-' * 20, 'Sequentially', '-' * 20)
    startS = time.time()
    vectorCal.getCenterPoint()
    equalResult = [None]
    vectorCal.calEuclidean(equalResult, 0)
    endS = time.time()
    totalS = endS - startS
    print(
        'Point A(' + str(vectorCal.x1) + ', ' + str(vectorCal.y1) + '), B(' + str(vectorCal.x2) + ', ' + str(
            vectorCal.y2) + ') and C(' + str(vectorCal.x3) + ', ' + str(vectorCal.y3) + '):')
    print(f'- Point center K: ({vectorCal.x}, {vectorCal.y})')
    print(f'- Euclidean around to center: {equalResult[0]}')
    time.sleep(0.5)

    print('-' * 20, 'Parallel', '-' * 20)
    startP = time.time()
    results = [None] * 3
    t1 = threading.Thread(target=vectorCal.getCenterPointCopy, args=(results, 0))
    t2 = threading.Thread(target=vectorCal.calEuclidean, args=(results, 2))
    t = [t1, t2]

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

    print(
        'Point A(' + str(vectorCal.x1) + ', ' + str(vectorCal.y1) + '), B(' + str(vectorCal.x2) + ', ' + str(
            vectorCal.y2) + ') and C(' + str(vectorCal.x3) + ', ' + str(vectorCal.y3) + '):')
    print(f'- Point center K: ({results[0]}, {results[1]})')
    print(f'- Euclidean around to center: {results[2]}')

    print('-' * 50)
    time.sleep(0.5)
    print('=' * 3 + '> Equal quality time: Sequentially ' + (
        '<' if totalS < totalP else '>') + ' Parallel ' + '<' + '=' * 3)


if __name__ == '__main__':
    print('-' * 10 + 'Input value vector', '-' * 10)
    x1 = float(input('Enter x1: '))
    y1 = float(input('Enter y1: '))
    x2 = float(input('Enter x2: '))
    y2 = float(input('Enter y2: '))
    x3 = float(input('Enter x3: '))
    y3 = float(input('Enter y3: '))
    processVector(x1, y1, x2, y2, x3, y3)
