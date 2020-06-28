import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8989))
sk.send('你好'.encode('utf-8'))
msg = sk.recv(1024).decode('utf-8')
print(msg)
sk.close()