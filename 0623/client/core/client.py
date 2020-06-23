from .auth_client import Auth
def main():
    auth_obj = None
    flag = False
    start_l = [('登录','login'),('注册','register'),('退出','exit')]
    for index ,item in enumerate(start_l):   #todo
        print(index+1,item[0])
    while not flag:
        try:
             num = int(input('>>>'))
             func_str = start_l[num-1][1]
        except:
              print('输入信息有误')
        if hasattr(Auth,func_str):
            auth_obj = Auth()
            func = getattr(auth_obj,func_str)
            flag = func()
        elif auth_obj:
            auth_obj.sk.close()
            exit()
        else:
            exit()