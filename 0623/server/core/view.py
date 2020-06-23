from .user import  User
import os
import pickle
from conf import setting
def login(msg):
    print('view',msg)
def register(msg):
    # info = {
    #     'username': username,
    #     'password': password,
    #     'operation': 'register',
    # }
    username = msg['username']
    user_obj = User(username)
    pickle_path = os.path.join(setting.pickle_path,username)
    with open(pickle_path,mode='wb') as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home)
    with open(setting.user_info,mode='a') as f:
         f.write('%s|%s|%s'%(msg['username'],msg['password'],pickle_path))
    print('view',msg)
