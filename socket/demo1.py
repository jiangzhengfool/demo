import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8898))  #把地址绑定到套接字
     #监听链接
sk.listen()
conn,addr = sk.accept() #接受客户端链接
while 1:
    ret = conn.recv(1024)  #接收客户端信息
    print(ret)       #打印客户端信息
    str1 = input()
    conn.send(bytes(str1,encoding='utf-8'))        #向客户端发送信息
conn.close()       #关闭客户端套接字
sk.close()        #关闭服务