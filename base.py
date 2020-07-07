#  coding:utf-8
import re
# print ('江')
# flag = 'true'R
# if flag:
#     print 'true'
# else:
#     print 'false'
# n = 0
# count = 0
# while n <= 100:
#     count += n
#     n += 1
# print count
# print True
# def get_middle(s):
#     #your code here
#     str1 = s
#     lens = len(s)
#     if lens % 2 == 1:
#         print str1[int(lens/2)]
#     else:
#         print str1[lens/2-1]+str1[lens/2]
#
# get_middle("abcdef")
# def find_short(s):
#     # your code here
#     arr = s.split(' ')
#     l = len(s)
#     for temp in arr:
#         if l > len(temp):
#             l = len(temp)
#     return l  # l: shortest word length
# print find_short('turns ot random test cases are easier than writing out basic ones')
# def is_isogram(string):
#     # your code here
#     count =[0]*26
#     if not string:
#         return True
#     string =string.lower()
#     lens =len(string)
#     n = 0
#     while n < lens:
#         temp = string[n]
#         n += 1
#         temp = ord(temp) - 97
#         count[temp] += 1
#         if count[temp] >= 2:
#             return False
#     return True
# print  is_isogram('ord')
# s = ''
# if not s:
#     print 'null'
# else:
#     print 'feikong'
#
# str = 'abc'
# print str.split(' ',3)
# a,b,c = 0 * 3
# print a,b,c
# a = {'name':{"jiang":'jian'}}
# a['name']['jiang'] = 'air'
# print a

# abc = 'abababbabab654'
# abc = re.sub ('[^1-9]','',abc)
#
# print abc
# def zeros(n):
#     num = 0
#     for i in range(1, n ):
#         n = (n * i)
#         while ((n % 10) == 0):
#             n = n / 10;
#             num += 1;
#         n = n % 10;
#
#     print(n,num)
#     return num
# zeros(30)
# def pig_it(text):
#     #your code here
#     arr = text.split()
#     for index,i in enumerate(arr):
#         if len(i) > 1 | i.isupper() | i.islower():
#             j = list(i)
#             t = j.pop(0)
#             j.append(t)
#             j.append('ay')
#             arr [index] = ''.join(j)
#
#     text =' '.join(arr)
#     print(text)
#     return text
# pig_it('Pig latin is cool !')
# def score(dice):
#     # your code here
#     count = 0
#     dice = sorted(dice)
#     print(dice)
#     if dice[0] == dice[2]:
#         n = dice[2] * 100
#         count += n * 10 if dice[2] == 1 else n
#         if (dice[3] == 5) | (dice[3] ==1):
#             count += dice[3] * 100 if dice[3] == 1 else dice[3] * 10
#         if (dice[4] == 5) | (dice[4] == 1):
#             count += dice[4] * 100 if dice[4] == 1 else dice[4] * 10
#     elif dice[2] == dice[4]:
#         n = dice[2] * 100
#         count += n * 10 if dice[2] == 1 else n
#         if (dice[0] == 5) | (dice[0] == 1):
#             count += dice[0] * 100 if dice[0] == 1 else dice[0] * 10
#         if (dice[1] == 5) | (dice[1] == 1):
#             count += dice[1] * 100 if dice[1] == 1 else dice[1] * 10
#     elif (dice[2] == dice[3])& (dice[2] == dice[1]):
#         n = dice[2] * 100
#
#         count += n * 10 if dice[2] == 1 else n
#         if (dice[0] == 5) | (dice[0] == 1):
#             count += dice[0] * 100 if dice[0] == 1 else dice[0] * 10
#         if (dice[4] == 5) | (dice[4] == 1):
#             count += dice[4] * 100 if dice[4] == 1 else dice[4] * 10
#         # print(count)
#     else:
#
#         for i in dice:
#             if i == 1:
#                 count += 100
#             if i == 5:
#                 count += 50
#     print(count)
#     return count

# score([1,2,2,6,6])
# def dig_pow(n, p):
#     # your code
#     s = str(n)
#     count =0
#     s = reversed(s)
#     for i in s:
#
#         count += int(i)**p
#         print(i)
#         p += 1
#     return count//n if (count % n==0) else -1
# print(dig_pow(89,1))
#
# def expanded_form(num):
#     ls = []
#     p = 1
#     while num > 0:
#         n = num % 10 * p
#         if n :
#             ls.append(str(n))
#         num = num // 10
#         p *= 10
#
#     return ' + '.join(reversed(ls))
# print(expanded_form(70304))
# def move_zeros(array):
#     t = [i for i in array if ((type(i) != int) & (type(i) != float) ) | (i!=0)]
#     return t + [0]*(len(array)-len(t))
#     #your code here

# seconds = 3600*24*365
# s = seconds % 60
# m = seconds // 60 % 60
# h = seconds // 3600 % 24
# d = seconds // 3600 // 24 % 365
# y = seconds // 3600 // 24 // 365
#
# print(s,m,h,d,y)
# def format_duration(seconds):
#     # your code here
#     num =['']*5
#     s = [0]*5
#     num[4] = se = str(seconds % 60)
#     num[3] = m = str(seconds // 60 % 60)
#     num[2] = h = str(seconds // 3600 % 24)
#     num[1] = d = str(seconds // 3600 // 24 % 365)
#     num[0] = y = str(seconds // 3600 // 24 // 365)
#     print(y,d,h,m,se)
#     s[0] = y + ' year' if y == '1' else y + ' years'
#     s[1] = d + ' day' if d == '1' else d + ' days'
#     s[2] = h + ' hour' if h == '1' else h + ' hours'
#     s[3] = m + ' minute' if m == '1' else m + ' minutes'
#     s[4] = se + ' second' if se == '1' else se + ' seconds'
#     ret = [s[i] for i in range(5) if int(num[i]) > 0]
#     print(s)
#     l = len(ret) >= 2
#     ret_str = ', '.join(ret)
#     i = ret_str.rfind(',')
#     ret_str = ret_str if not l else (ret_str[:i] + ' and ' + ret_str[i+2:])
#     print(ret_str)
#     return ret_str
#
#
# print(format_duration(62))
#
# print(1 == '1')
#
# b = "\n".join([
#   ".W.",
#   ".W.",
#   "W.."
# ])
#
# # print(type(b))
# def path_finder(maze_s,x=0,y=0):
#     maze = maze_s.split()
#     l = len(maze)
#     #print(x,y,l)
#     #print((l -1) == x)
#     if (x == y) and ((l -1) == x):
#         print((x == y) and ((l -1) == x))
#         return True
#     if x+1 < l and maze[x+1][y]!='W':
#         #print(maze[x+1][y])
#        return path_finder(maze_s,x+1,y)
#     if y + 1 < l and maze[x][y+1]!= 'W':
#         return path_finder(maze_s, x , y+1)
#     if x-1 < l and maze[x-1][y]!='W':
#         #print(maze[x+1][y])
#        return path_finder(maze_s,x-1,y)
#     if y - 1 < l and maze[x][y-1]!= 'W':
#         return path_finder(maze_s, x , y-1)
#
#     return False
#
# a = "\n".join([
#     '.W...',
#     '.W...',
#     '.W.W.',
#     '...W.',
#     '...W.'])
#
#
# print(path_finder(a))
# def next_smaller(n):
#     s = list(reversed(str(n)))
#     for index,i in enumerate(s):
#         for j in range(index,len(s)):
#             if s[index] < s[j]:
#                 t = s.pop(index)
#                 s.insert(j,t)
#                 return ''.join(reversed(s))
#     return -1
# print(next_smaller(127))

# def narcissistic( value ):
#     s = str(value)
#     l = len(s)
#     arr = [s,'is','narcissistic']
#     count = 0
#     for i in s:
#         count += int(i)**l
#     if count == value :
#         arr.insert(2,'not')
#     return ' '.join(arr)
#     # Code away
# narcissistic(371)
# a = str(hex(148))
# print(hex(148))
# print(a[-2:])
# def rgb(r, g, b):
#     # your code here :
#     r = 0 if r < 0 else r
#     g = 0 if g < 0 else g
#     b = 0 if b < 0 else b
#     r = 255 if r > 255 else r
#     g = 255 if g > 255 else g
#     b = 255 if b > 255 else b
#     #print(r, g, b)
#     r = hex(r)
#     g = hex(g)
#     b = hex(b)
#     if len(r) == 3:
#         r = r[0:2]+'0'+r[2:]
#     if len(g) == 3:
#         g = g[0:2]+'0'+g[2:]
#     if len(b) == 3:
#         b = b[0:2] + '0' + b[2:]
#     print(r, g, b)
#     return r[2:].upper() + g[2:].upper() + b[2:].upper()
#
# print(rgb(255,255,125))
#
# print(type(hex(55)))
# def domain_name(url='http://www.zombie-bites.com'):
#     i0 = url.find('https')
#     i1 = url.find('.')
#     i2 = url.rfind('.')
#     print(i0,i1)
#     if i0 >= 0 :
#          s =url[8:i1]
#          print(0,s)
#     else:
#         s = url[7:i1]
#     s = s if 'www' != s else url[i1+1:i2]
#     return s
# domain_name()

# def domain_name(url='http://youtube.com'):
#     i1 = url.find('.')
#     i2 = url.rfind('.')
#     i0 = url.find('https')
#     if i1 != i2 :
#         s = url[i1 + 1:i2]
#     else:
#         if i0 >= 0:
#             s = url[8:i1]
#             print(0, s)
#         else:
#             s = url[7:i1]
#     print(s)
#     return s
#
# domain_name()

'http://google.co.jp'
'icann.org'
'http://sjllixpmk0ew0bdgfbjam9my.tv/default.html'
# def domain_name(url='www.xakep.ru'):
#     i0 = url.find(':')
#     i1 = url.find('.')
#     print(i0,i1)
#     if i0 > 0:
#         s = url[i0+3:i1]
#         if s == 'www':
#             s =url[i1+1:]
#             i2 =s.find('.')
#             s = s[:i2]
#     else:
#         s = url[:i1]
#         if s == 'www':
#             s =url[i1+1:]
#             i2 =s.find('.')
#             s = s[:i2]
#     return s
# print(domain_name())
#
#

# def sum_of_intervals(intervals=[
#    [1,4],
#    [7, 10],
#    [3, 5]
# ]):
#
#
#     return sum([i[1]-i[0] for i in intervals])
#
# print(sum_of_intervals())
#
# 2、求中位数<br>用having子句进行自连接求中位数<br>
# 第一步-- 将集合里的元素按照大小分为上半部分、下班部分 两个子集，
# 求其交集（无论聚合数据的数目是 奇数 偶数）
# select  t1.income
# from gradutes t1 , gradutes t2
# group by t1.income
# having sum(case when t2.income >=t1.income then 1 else 0 end) >= count(*)/2<
# and sum(case when t2.income <=t1.income then 1 else 0 end) >= count(*)/2;<br>
# 第二步 -- 将上下部分集合求得的交集，去重，然后求平均，得到中值<br>select avg(distinct income)<br>from ( select t1.income<br>　　　　from gradutes t1,gradutes t2<br>　　　　group by t1.income<br>　　　　having sum(case when t2.income >= t1.income then 1 else 0) >= count(*)/2<br>　　　　　　and sum (case when t2.incomme <= t1.income then 1 else 0 ) >= count(*)/2) as tmp
def sum_triangular_numbers(n):
    # your code here
    for i in range(1,10):
        pass
    return sum((1 + i) * i / 2 for i in range(1,n))