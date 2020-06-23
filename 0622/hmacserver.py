import socket
import os
import hmac
sk = socket.socket()
screct_key = b'egg'
sk.bind(('127.0.0.1',8989))
sk.listen()
def check_conn():

    msg = os.urandom(32)
    conn.send(msg)
    h = hmac.new(screct_key,msg,digestmod='md5')
    digst = h.digest()
    client_digest = conn.recv(1024)
    return hmac.compare_digest(digst,client_digest)

conn,addr = sk.accept()
res = check_conn()
print(res)