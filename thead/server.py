import socket
from multiprocessing import Process

sk = socket.socket()
sk.bind(('127.0.0.1',8989))
sk.listen()
def myserver(conn):
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    ret = input('>>>').encode('utf-8')
    conn.send(ret)
    conn.close()
if __name__ == '__main__':
    while 1:
        conn,addr = sk.accept()
        p = Process(target=myserver,args = (conn,))
        p.start()
    sk.close()