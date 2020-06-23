import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

from  core  import client

if  __name__ == '__main__':
     # print(os.getcwd())
     # print(os.path.dirname(os.getcwd()))
     client.main()
