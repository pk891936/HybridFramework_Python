st = 'A7B1R3'
#output =ABR137
alpha = []
num = []
for i in st:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(i)
my_list = sorted(alpha)+sorted(num)
print(''.join(my_list))
