import socket
import json
import struct
import  os
sk = socket.socket()
sk.connect(('127.0.0.1',8989))
buffer = 40960
head = {
    'filepath':'/Users/a10.11.5/Downloads/照花台.mp4',
    'filename':'照花台.mp4',
    'filesize':17819003
}
json_head = json.dumps(head)
bytes_head = json_head.encode('utf-8')
head_len = len(bytes_head)
pack_len  = struct.pack('i',head_len)
# print(bytes_head)
sk.send(pack_len)
sk.send(bytes_head)
file_size = os.path.getsize(head['filepath'])
head['file_size'] = file_size

with open(head['filepath'],mode='rb') as f:
    while file_size > 0:
        print(file_size)
        if file_size >= buffer:
            bytes = f.read(buffer)
            sk.send(bytes)
            file_size -=buffer
        else:
            bytes = f.read(file_size)
            sk.send(bytes)
            break

sk.close()

