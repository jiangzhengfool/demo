import socket
import json
import struct
import  os
sk = socket.socket()
sk.connect(('127.0.0.1',8989))
buffer = 1024
head = {
    'filepath':'/Users/a10.11.5/Downloads/pycharm-community-2020.1.2.dmg',
    'filename':'pycharm.dmg',
    'filesize':None
}
filesize = os.path.getsize(head['filepath'])
head['filesize'] = filesize
print(head['filesize'])
json_head = json.dumps(head)
bytes_head = json_head.encode('utf-8')
head_len = len(bytes_head)
pack_len  = struct.pack('i',head_len)
# print(bytes_head)
sk.send(pack_len)
sk.send(bytes_head)


with open(head['filepath'],mode='rb') as f:
    while filesize > 0:
        # print(file_size)
        if filesize >= buffer:
            bytes = f.read(buffer)
            sk.send(bytes)
            filesize -=buffer
        else:
            bytes = f.read(filesize)
            sk.send(bytes)
            break

sk.close()

