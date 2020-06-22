import  socket
sk = socket.socket()
sk.bind('127.0.0.1',8989)
sk.listen()
conn,addr = sk.accept()

conn.recv()
conn.send()
conn.close()
sk.close()