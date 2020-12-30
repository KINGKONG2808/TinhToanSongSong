import threading
import time
import random

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, results):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.results = results

    def run(self):
        print("Starting " + self.name + "\n")
        print_time(self.name, 3, self.counter, self.results)
        print("Exiting " + self.name + "\n")


def print_time(threadName, counter, delay, results):
    i = 0
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        result = random.randint(1, 10)
        while result in results:
            result = random.randint(1, 10)
        results[i] = result
        i += 1
        print("%s: %s \n" % (threadName, str(result)))
        counter -= 1


# Create new threads
results = [None] * 9
thread1 = myThread(1, "Thread-1", 1, results)
thread2 = myThread(2, "Thread-2", 2, results)
thread3 = myThread(3, "Thread-3", 3, results)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

