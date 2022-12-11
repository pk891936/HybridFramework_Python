print('***********Duplicates in integer******')
input = 1234567
s =str(input)
for i in s:
    if s.count(i)>1:
        print('Duplicate digits exist')
        break
    else:
        print('No Duplicate exist')
        break

print('***********Duplicates in integer without  using string  datatype******')

n = 12345676367
temp = 0
a = []
while n >0:
    r = n % 10
    n = n // 10
    print(r)
    a.append(r)
print(a)
for i in a:
    if a.count(i) > 1:
        print('Duplicate digits exist')
        break
    else:
        print('No Duplicate exist')
        break