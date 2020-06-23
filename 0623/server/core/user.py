from conf import setting
import  os
class  User:
    def __init__(self,name):
        self.name = name
        self.home = os.path.join(setting.homepath,name)
        self.cur_path = self.home
        self.disk_space = 20*2**30