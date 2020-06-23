import os
import socketserver
import sys
sys.path.append(os.path.dirname(os.getcwd()))


from  core  import server
from  conf  import setting
if  __name__== '__main__':
    print('ok')
    server = socketserver.ThreadingTCPServer(setting.addr,server.Myftpserver)
    server.serve_forever()
