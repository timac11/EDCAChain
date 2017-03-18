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