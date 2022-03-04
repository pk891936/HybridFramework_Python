
print("*************Frequency of each Character in a string using Set and string.Count***************")
s = "mississippi"

def no(i):
    return s.count(i)
a = sorted(set(s))
print(a)

for i in a:
    print(i,"count=",no(i))

print("*************Frequency of each Character in a string Using Dict ***************")

chr_freq = {}
for i in s:
    if i in chr_freq:
        chr_freq[i] += 1

    else:
        chr_freq[i] = 1


print("Count of all characters in string is :\n "+str(chr_freq))


