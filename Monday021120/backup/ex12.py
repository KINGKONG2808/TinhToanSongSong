import threading
import time
from datetime import datetime


def textNumber(i):
    switcher = {
        0: 'không',
        1: 'một',
        2: 'hai',
        3: 'ba',
        4: 'bốn',
        5: 'năm',
        6: 'sáu',
        7: 'bảy',
        8: 'tám',
        9: 'chín'
    }
    return switcher.get(i, "null")


class getDetailNumber:
    def __init__(self, number=1523):
        self.number = number

    def getThousandsDigit(self):
        return int(self.number / 1000)

    def getHundredsDigit(self):
        return int((self.number % 1000) / 100)

    def getTensOfDigit(self):
        return int(self.number % 1000 % 100 / 10)

    def getUnitRowDigit(self):
        return int(self.number % 1000 % 100 % 10)

    def getThousandsDigitText(self, results, index):
        thousandDigit = getDetailNumber.getThousandsDigit(self)
        if self.number < 1000:
            strResult = ''
        else:
            strResult = textNumber(thousandDigit) + ' nghìn'
        results[index] = strResult

    def getHundredsDigitText(self, results, index):
        hundredsDigit = getDetailNumber.getHundredsDigit(self)
        if self.number < 100:
            strResult = ''
        else:
            strResult = textNumber(hundredsDigit) + ' trăm'
        results[index] = strResult

    def getTensOfDigitText(self, results, index):
        tensOfDigit = getDetailNumber.getTensOfDigit(self)
        if self.number < 10:
            strResult = ''
        elif tensOfDigit == 0:
            strResult = 'linh'
        elif tensOfDigit == 1:
            strResult = 'mười'
        else:
            strResult = textNumber(tensOfDigit) + ' mươi'
        results[index] = strResult

    def getUnitRowDigitText(self, results, index):
        results[index] = textNumber(getDetailNumber.getUnitRowDigit(self))


def convertNumberToText(number):
    print('*'*20, 'Get detail number', '*'*20)
    detail = getDetailNumber(number)

    print('-'*20, 'Sequentially', '-'*20)
    startS = time.time()
    equalResult = [None]*4
    detail.getThousandsDigitText(equalResult, 0)
    detail.getHundredsDigitText(equalResult, 1)
    detail.getTensOfDigitText(equalResult, 2)
    detail.getUnitRowDigitText(equalResult, 3)
    endS = time.time()
    totalS = endS - startS
    print('=> Result run by sequentially: ' + ' '.join(equalResult) + f" in {format(totalS, '.10f')}s")
    time.sleep(0.5)

    print('-' * 20, 'Parallel', '-' * 20)
    startP = time.time()
    results = [None]*4
    t1 = threading.Thread(target=detail.getThousandsDigitText, args=(results, 0))
    t2 = threading.Thread(target=detail.getHundredsDigitText, args=(results, 1))
    t3 = threading.Thread(target=detail.getTensOfDigitText, args=(results, 2))
    t4 = threading.Thread(target=detail.getUnitRowDigitText, args=(results, 3))
    t = [t1, t2, t3, t4]

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
    print(f'=> Result convert from {detail.number} to text: ' + ' '.join(results) if results[0] is not None else '')

    # print('-' * 50)
    # time.sleep(0.5)
    # print('=' * 3 + '> Equal quality time: Sequentially ' + ('<' if totalS < totalP else '>') + ' Parallel ' + '<' + '=' * 3)


if __name__ == '__main__':
    number = int(input('Enter the number: '))
    while number > 9999:
        print('Invalid size of number (<10000)')
        number = int(input('Enter the number again: '))
    convertNumberToText(number)
