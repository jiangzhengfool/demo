import  socketserver
import json
from conf import setting
from  .import view
class Myftpserver(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.my_recv()
        op_str = msg['operation']
        if hasattr(view,op_str):
            func = getattr(view,op_str)
            ret = func(msg)
            self.my_send(ret)


    def my_recv(self):
        msg = self.request.recv(1024)
        print(msg)
        msg = msg.decode(setting.code)

        msg = json.loads(msg)
        return msg
    def my_send(self,msg):
        msg = json.dumps(msg).encode(setting.code)
        self.request.send(msg)
