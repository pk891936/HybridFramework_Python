n = int(input("Enter a number: "))
count =0
temp = n
while n>0:
    if n%2 ==0:
        n=n//2
        count=count+1
        print("n=",n,"......count=",count)
    else :
        break
if temp == 2**count:
    print("{} is power of 2,{}".format(temp,count))
else:
    print("Not power of 2")


