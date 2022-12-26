import time
from threading import Thread
import threading

a = 0

# cac thread chay // rieng re nhau
# cac luong co the su dung chung 1 taif nguyen

def thread1():
    print(f"t1 is running in thread: {threading.current_thread().name}")

    for i in range(10):
        print(f"Thread 1: {i} in {threading.current_thread().name}")
        time.sleep(1)

def thread2():
    print(f"t2 is running in thread: {threading.current_thread().name}")

    for i in range(10):
        print(f"Thread 2: {i} in {threading.current_thread().name}")
        time.sleep(1.5)


print(f"Start thread main {threading.current_thread().name}")

t1 = Thread(target=thread1)
t2 = Thread(target=thread2)


t1.start()
t2.start()

# thuc hien join luong 1 vao luong main
t1.join()

# thuc hien join luong 2 vao luong main
t2.join()

print("Stop thread main")
