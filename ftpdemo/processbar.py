import time
import math
# size = 100
# for i in  range(size):
#     time.sleep(0.1)
#     percent = int((i) / size * 20)
#     print('\r%s %%: %s' % (i, '*' * percent),end='', flush=False)

#'\r%s%% : %s\n' % (i, '*' * char_num)
def print_percent(i,size):
    i = math.ceil(i/size*100)
    percent = int((i) / size * 100)

    print('\r%s %%: %s' % (i, '*' * percent), end='', flush=False)

print_percent(50,100)
print_percent(70,100)