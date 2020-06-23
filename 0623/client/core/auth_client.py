from .skclient import  MySocketclient
import json
class Auth:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance =  object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.socket = MySocketclient()
    def login(self):
        username = input('username').strip()
        password = input('password').strip()
        if len(username) & len(password):
            info = {
               'username':username,
                'password':password,
                'operation':'login'
            }
            self.socket.mysend(info)
        ret = self.socket.sk.recv(1024)

    def register(self):
        username = input('username').strip()
        password = input('password').strip()
        password_ensure = input('password_ensure').strip()
        if password != password_ensure:
            return False
        if len(username) & len(password) :
            info = {
                'username': username,
                'password': password,
                'operation': 'register',
            }
            print('info',info)
            self.socket.mysend(info)
        ret = self.socket.sk.recv(1024)