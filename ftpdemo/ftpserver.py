import socket
import struct
import json
import math
buffer = 1024

def print_percent(i,size):
    percent = int((i) / size * 20)
    i = math.ceil(i/size*100)
    print('\r%d %%: %s' % (i, '*' * percent), end='', flush=False)


sk = socket.socket()
sk.bind(('127.0.0.1',8989))
sk.listen()
conn,addr = sk.accept()

# 接受
pack_len = conn.recv(4)

head_len = struct.unpack('i',pack_len)[0]
json_head = conn.recv(head_len).decode('utf-8')
print(json_head)
head = json.loads(json_head)
filesize = int(head['filesize'])
size = filesize

with open(head['filename'],mode='wb') as f:
    while filesize > 0:
        print_percent(size-filesize,size)
        if filesize >= buffer:
            bytes = conn.recv(buffer)
            filesize -= buffer
            f.write(bytes)
        else:
            filesize = 0
            conn.recv(filesize)
            f.write(bytes)
            break

conn.close()
sk.close()