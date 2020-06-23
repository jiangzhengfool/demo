import socket
sk =socket.socket()
sk.connect(('127.0.0.1',8989))
while 1 :
    msg = input('>>>')
    if msg.strip() == b'q':
        sk.send('bye')
        sk.close()
        break
    else:
        sk.send(msg.encode('utf-8'))
        info = sk.recv(1024)
        print(info.decode('utf-8'))
