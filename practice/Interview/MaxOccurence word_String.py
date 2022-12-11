str = 'abc is cde abc is nmot efg efg is lmn efg is not  ahd'

def count_word(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word]=1
    return counts
counts = count_word(str)
print(counts)
m = set(counts.values())
values = sorted(m)
max = values[-1]
print(max)
for key in counts.keys():
    if counts[key]==max:
        print(key)

print('**********Second method**********')
def count_word(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word]=1
    return counts
counts = count_word(str)
counts_x = sorted(counts.items(), key=lambda kv:kv[1])
print(counts_x)
print(counts_x[-1][0])






