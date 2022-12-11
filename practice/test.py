capitals = {"India":"Delhi", "Afghanistan":"Kabul", "Nepal":"Khatmandu"}

def check(country,capital):
    if country in capitals.keys():
        if capitals[country]==capital:
            print("True")

        else:
            print("False")

check("India","Delhi")

d={'A':10,'B':10,'C':239}
prod=1
for i in d:
    print(i)
    prod=prod*d[i]
print(prod)


test_string="mississippi"
l=list(test_string)
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))

print("*********startletter:word ****************")
test_string=input("Enter string:")
l=test_string.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)