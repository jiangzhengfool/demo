import socket

'''
http 协议
ftp 
smtp
    
'''
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(5)
conn,addr = sk.accept()


res = conn.recv(1024*8)
print(res)
conn.send(b'http/1.1 200 ok\r\n\r\n')
conn.send(b'123123')

conn.close()
sk.close()