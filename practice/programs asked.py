print("Program to replace . with - from the given list of strings")
import re
print("Replace . with - using re")
s =["11.22.334.444","32.34.112.23"]
for i in s:
    print(re.sub('..', "-", i))

for i in s:
    x= i.replace('.','-')
    print(x)

print("Program to remove duplicates from the given list")

print("********remove duplicates from the given list using loop and temp variable**************")
l = [1,2,3,4,5,1,1,2,3,22,44,4]
r = []
for i in l:
    if i not in r:
        r.append(i)
print("list after removing duplicates: ", r)

print("Removing duplicates using set : ",list(set(l)))

print("Remove duplicates using OrderedDict.fromkeys")
from collections import OrderedDict
test_list = [1, 5, 3, 6, 3, 5, 6, 1]

res = list(OrderedDict.fromkeys(test_list))

# printing list after removal
print("The list after removing duplicates : " , res)

# using collections.OrderedDict.fromkeys()
# to remove duplicated
# from list
print("Removing duplicates using loop without temp list:")
def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

s = [1,2,3,4,5,1,1,2,3,22,44,4]
remove_dup(s)
print("Removing duplicates using loop:",s)

print("******calculator and scientific calculator using Inheritence*********")

class calculator:
    def __init__(self,a ,b):
        self.a = a
        self.__b = b
    def add(self):
        return self.a + self.__b
    def sub(self):
        return self.a - self.__b
    def multiply(self):
        return self.a * self.__b
    def div(self):
        return self.a / self.__b

t =calculator(20,10)
print(t.add())
print(t.sub())
print(t.multiply())
print(t.div())

class scientfic_Cal(calculator):
    def __init__(self, a, b):
        #super().__init__(a, b)
        calculator.__init__(self, a,b)


    def p(self):
        print("sine value: =", self.a)


t=scientfic_Cal(20,10)
t.p()

print("**********Dictionary Comprehension***********")
keys = [1,2,3,4,5]
values =['a','b','c','d','e']
dic = {k:v for (k,v) in zip(keys,values)}
print(dic)

d={n:n**3 for n in range(1,10) if n**3%4 ==0}
print(d)
