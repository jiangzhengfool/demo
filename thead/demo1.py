# def divisors(integer):
#     return [ i for i in range(2,integer-1) if integer % i == 0]
#
# print(divisors(10))
# def validate_pin(pin):
#     # return true or false
#     lens = len(pin)
#     if lens not in [4,6]:
#         return False
#     for i in pin:
#         if not i.isdigit():
#             return False
#
#     return True
# print(validate_pin('223a'))
arr = [1,5,2,7,4]
# info = arr.pop()
# print(arr)
# arr.sort()
# arr.append(info)
# print(arr)
# arr_new = [ i for i in arr if i % 2 ==1 ]
# arr_new.sort(reverse=True)
# for index,i in enumerate(arr):
#     if i % 2 == 1:
#         arr[index] = arr_new.pop()
# print(arr_new)
# print(arr)
# trantab = str.maketrans("","","aeiouAEIOU")  # 创建字符映射转换表，并删除指定字符
#
# test = "This website is for lxxxosers LOL!"
#
# print(test.translate(trantab))
# str1 = 'de'
# print('#'*(len(str1)-4)+str1[-4:])
num = 123456789
arr = (list(str(num)))
arr.sort(reverse=True)
print(''.join(arr))
from  threading import Thread
Thread()
