import socket
sk = socket.socket()           # 创建客户套接字
sk.connect(('127.0.0.1',8898))   # 尝试连接服务器
while 1:
    str1 = input()
    sk.send(bytes(str1, encoding='utf-8'))
    ret = sk.recv(1024)         # 对话(发送/接收)
    print(ret)
sk.close()            # 关闭客户套接字