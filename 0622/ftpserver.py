import socket
import struct
import json
buffer = 40960
sk = socket.socket()
sk.bind(('127.0.0.1',8989))
sk.listen()
conn,addr = sk.accept()

# 接受
pack_len = conn.recv(4)

head_len = struct.unpack('i',pack_len)[0]
json_head = conn.recv(head_len).decode('utf-8')

head = json.loads(json_head)
filesize = head['filesize']
with open(head['filename'],mode='wb') as f:
    while filesize > 0:

        if filesize >= buffer:
            bytes = conn.recv(buffer)

            f.write(bytes)
        else:
            conn.recv(filesize)
            f.write(bytes)
            break
conn.close()
sk.close()