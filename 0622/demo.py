import socket

'''
http 协议
ftp 
smtp
    
'''
sk = socket.socket()
sk.bind(('127.0.0.1',8989))
sk.listen()
conn,addr = sk.accept()
while 1:
    cmd = input('>>>')
    conn.send(cmd.encode('gbk'))
    res = conn.recv(1024)
    print(res.decode('gbk'))
conn.close()
sk.close()