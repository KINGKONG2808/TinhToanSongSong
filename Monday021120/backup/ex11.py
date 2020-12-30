import threading
import time
from datetime import datetime


class math_simple:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def plus(self):
        print('a + b = ', self.a + self.b)

    def minus(self):
        print('a - b = ', self.a - self.b)

    def multiply(self):
        print('a * b = ', self.a * self.b)

    def division(self):
        print('a / b = ', float(self.a / self.b))

    def mod(self):
        print('a % b = ', self.a % self.b)


print('*' * 20, 'Example 1.1:', '*' * 20)
a = int(input('Enter a: '))
b = int(input('Enter b: '))
mathSimple = math_simple(a, b)

print('-' * 20, 'Sequentially', '-' * 20)
startS = time.time()
mathSimple.plus()
mathSimple.minus()
mathSimple.multiply()
mathSimple.division()
mathSimple.mod()
endS = time.time()
totalS = format(endS - startS, '.5f')
print(f'Total time sequentially: ', format(totalS, '.10f'))

print('*' * 20, 'Wait a minus', '*' * 20)
time.sleep(0.5)

print('-' * 20, 'Parallel', '-' * 20)
startP = time.time()
t1 = threading.Thread(target=mathSimple.plus())
t2 = threading.Thread(target=mathSimple.minus())
t3 = threading.Thread(target=mathSimple.multiply())
t4 = threading.Thread(target=mathSimple.division())
t5 = threading.Thread(target=mathSimple.mod())

t = [t1, t2, t3, t4, t5]

print('-'*20 + 'Detail thread open/end time' + '-'*20)
for i in range(len(t)):
    print(f"\t- Thread {i+1} start in {datetime.now().strftime('%H:%M:%S.%f')}")
    t[i].start()

for i in range(len(t)):
    t[i].join()
    print(f"\t- Thread {i+1} end in {datetime.now().strftime('%H:%M:%S.%f')}")

endP = time.time()
totalP = format(endP - startP, '.5f')
print(f'=> Total time parallel: ', format(totalP, '.10f'))

print('-'*50)
time.sleep(0.5)
print('='*3 + '> Equal quality time: Sequentially ' + ('<' if totalS < totalP else '>') + ' Parallel ' + '<' + '='*3)
