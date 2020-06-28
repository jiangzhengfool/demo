from   multiprocessing  import  Queue,Process
import time
def produce(q):
    q.put('gg')

if __name__ == '__main__':
    q = Queue(6)
    p = Process(target=produce,args=(q,))
    p.start()
    time.sleep(2)
    print(q.get())