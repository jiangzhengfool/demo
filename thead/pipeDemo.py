from multiprocessing import Pipe

conn1,conn2 = Pipe()
conn1.send('介质')
conn2.send('aa')
print(conn2.recv())
print(conn1.recv())