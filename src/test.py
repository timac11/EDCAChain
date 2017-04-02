#fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
#print(fib(31))
#n = int(input())
#k = 0
#for i in range(0, n):
#    k = k + int(input())
#print(k)

#x = [1, 2, 3]
#y = x
#y.append(4)

#s = "123"
#t = s
#t = t + "4"
#y = "4"
#print(str(x) + " " + s)
#objects = [1,2,3,3,4,5,6,5,5]
#ans = 0
#flag = 0
#objectFlag = 0
#aSet = set()
#for obj in objects:
#    aSet.add(obj)
#print(len(aSet))
###########################################################
'''
newList = []
# = 0
for obj in objects:
    for newObj in newList:
       if obj is newObj:

             flag = 1
   if flag == 0:
        newList.append(obj)
    flag = 0
ans = 0
for newObj in newList:
    ans = ans + 1
print (ans)
'''
#import self as self

'''
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        if (x + 1) % 5 == 0:
            return x + 1
        else:
            if (x + 2) % 5 == 0:
                return x + 2
            else:
                if(x+3) % 5 == 0:
                    return x + 3
                else:
                    return x + 4
print (closest_mod_5(13))
'''
'''
def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res
print(s(0,31,0))
'''

def Sochit (n,k):
    if k>n:
        return 0
    else:
        if n>=k and k!=0:
            return Sochit (n-1,k) + Sochit(n-1,k-1);
        else:
            return 1
print (Sochit(10,1))



class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
    def can_add(self, v):
        if self.capacity - self.count < v:
            return False
        else:
            return True
    def add(self, v):
        self.count = self.count + v

class Buffer:
    def __init__(self):
        self.list = []
    def add(self, *a):
        for elem in a:
            self.list.append(elem)
            if len(self.list) == 5:
                sum = 0
                for cur_elem in self.list:
                    sum = sum + int(cur_elem)
                print(sum)
        self.list.append(a)
    def get_current_part(self):
        return self.list

# import datetime
# list = input().split()
# year = list[0]
# month = list[1]
# day = list[2]
# data = datetime.date(int(year), int(month), int(day))
# days = datetime.timedelta(days=int(input()))
# newDate = data + days
# print(newDate.year,newDate.month,newDate.day)

#import simplecrypt
#############################################################################################
# class multifilter:
#
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         return pos >= neg
#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         return pos >= 1
#     def judge_all(pos, neg):
#         return neg == 0
#         # допускает элемент, если его допускают все функции (neg == 0)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.pos = 0
#         self.neg = 0
#         self.newPosled = []
#         for iterator in iterable:
#             self.pos = 0
#             self.neg = 0
#             for func in funcs:
#                 if func(iterator):
#                     self.pos = self.pos + 1
#                 else:
#                     self.neg = self.neg + 1
#             #if pos > neg:
#             #    self.newPosled.append(iterator)
#             #else:
#             if judge(self.pos, self.neg):
#                 self.newPosled.append(iterator)
#
#
#         # iterable - исходная последовательность
#         # funcs - допускающие функции
#         # judge - решающая функция
#
#     def __iter__(self):
#         return iter(self.newPosled)
##################################################################################################

# def primes():
#     def isSimple(n):
#         d = n - 1
#         while d > 1:
#             if n % d == 0:
#                 return False
#             d -= 1
#         return True
#     for i in range(1, 10000):
#         if isSimple(i):
#             yield i
#####################################################################################################
# f1 = open("file.txt",'r')
# f2 = open("filecopy.txt", 'w')
# line = []
# for i in f1:
#     line.append(i)
# for i in range(len(line)):
#     f2.write(line.pop())
# f1.close()
# f2.close()
######################################################################################################
def mod_checker(x, mod=0):
    return lambda y: y % x == mod

a[lower : : upper] = []
a[lower + offset:upper + offset] = []
a[lower:upper], a[lower:upper:], a[lower::step] = []
a[lower + offset : upper + offset] = []
a[lower+offset : upper+offset] = []

