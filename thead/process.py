from multiprocessing import Process
import time
import os
def func(*args):
    # for i in range(100):
    #     time.sleep(0.1)
        print(os.getppid())
        print(args)
        # print(os.getpid())
        # print('func'+str(i))
def funk():
    # for i in range(100):
    #     time.sleep(0.1)
        print(os.getpid())
if __name__ == '__main__':
    p = Process(target=func,args=(4,4,4,66))
    p1 =Process(target=funk)
    print(os.getpid())
    # p1.start()
    p.start()
    os.walk()
    p.join(p1)