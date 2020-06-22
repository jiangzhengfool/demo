import  socket
import  subprocess
sk = socket.socket()
sk.connect(('127.0.0.1',8989))
while 1:
    cmd = sk.recv(1024).decode('gbk')
    if cmd  == 'q':
        sk.send(b'q')
        break
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    sk.send(res.stdout.read())
    sk.send(res.stderr.read())