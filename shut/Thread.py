from threading import Thread
from time import sleep

def func():
    for i in range(10):
        print(f"from 1 thread: {i}")
        sleep(0.99)

th = Thread(target=func)
th.start()
#func()

for i in range(10):
    print(f"from 222222 thread: {i}")
    #print("from 222222 thread:",i)
    #print(i)
    #print(i+i)
    #print("from 222222 thread: %s" % i)
    sleep(1)


print("Stop")