import  socket
import json
class MySocketclient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',8989))
    def mysend(self,info):
         info_info = json.dumps(info)
         self.sk.send(info_info.encode('utf-8'))