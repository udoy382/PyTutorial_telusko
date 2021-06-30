from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

# t1.run()
t1.start()
sleep(0.2)
# t2.run()
t1.start()

t1.join()
t2.join()
print("by")

#       show some error --> RuntimeError: threads can only be started once