import socket
import hmac
screct_key = b'egg'
sk =socket.socket()
sk.connect(('127.0.0.1',8989))
msg = sk.recv(1024)
h = hmac.new(screct_key,msg,digestmod='md5')
digst = h.digest()
sk.send(digst)
sk.close()