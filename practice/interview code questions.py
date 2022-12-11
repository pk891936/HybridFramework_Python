
print('******program to find least positive  integer from given input list*********')
#input = [1,-1,3,7,8,0,2,5,-6]
input = [3,7,-1,8,9,10]
l = [i for i in range(1,max(input))]
print(l)

for i in l:
    if i not in input:
        print('missing least +ve integer', i)
        break

print('******program to print prime numbers between 100 and 200*********')
for i in range(100,200):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print(i, end=' ')

print()
print('******program to sort a list without using sort function******')
data_list = [24,55,78,64,35,24,23,22,12,11,3,2,1]
new_list = []
while data_list:
    min = data_list[0]
    for i in data_list:
        if i>min:
            min = i
    new_list.append(min)
    data_list.remove(min)
print(new_list)

print('***********program to write fibonocii series*********')

def F(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return F(n-1)+F(n-2)
for i in range(12):
    print(F(i),end=' ')

print('***********program to print list in reverse order*********')
print(input[::-1])

print('******program to find string palindrome or not*********')
s = 'malayalam'
if s == s[::-1]:
    print(s,'is palindrome')
else:
    print(s, 'is not palindrome')

print('******program to print set of duplicates from a list*********')

l=[1,1,22,3,4,5,6,33,33,22,5,895,8,5,4,78]
print(set([i for i in l if l.count(i)>1]))

print('******program to print no. of words in a sentence*********')
s = 'python is a program language and it is very useful to code in python'
wcount = 0
print(len(s.split()))

print('******program to search an element in an array*********')
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    print('element not exist in array')

l = [1,2,3,4,5,6,7,8,9]
print('index of element:', search(l,4))