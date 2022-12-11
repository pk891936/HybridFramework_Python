st = 'aaaabbbccdzzzzzzz'
#output =4a3b2c1d
char = st[0]
count =0
new_str = ''
for ch in st:
    if ch == char:
        count = count+1
    else:
        new_str = new_str+str(count)+char
        count =1
        char = ch
new_str = new_str+str(count)+char
print(new_str)
