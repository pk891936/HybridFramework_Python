l = [14,33,95,-1,-6,21]


def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax

def lowestNumber(l):
    myMin = l[0]
    for num in l:
        if myMin > num:
            myMin = num
    return myMin
print(highestNumber(l))
print(lowestNumber(l))

a = []
def secondLargest(l):
    max = l[0]
    for num in l:
        if max < num:
            max = num
        if max not in a:
            a.append(max)
            print(a)
    return a

print(secondLargest(l)[-2])

