import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            msg = self.request.recv(1024).decode('utf-8')
            print(msg)
            if msg == 'q':
                self.request.close()
                break
            info =input('>>>')
            self.request.send(info.encode('utf-8'))

if __name__ =='__main__':

    server = socketserver.ThreadingTCPServer(('127.0.0.1',8989),Myserver)
    server.serve_forever()
    print(socketserver)