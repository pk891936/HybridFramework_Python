import csv


"""
111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http:// www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.123 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http:// www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.123 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 200 9332 "http:// www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.123 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 200 207 "http:// www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
"""



with open("abcd.txt", mode='r') as f:
    data = f.readlines()
    with open("data.csv", mode='w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(['Method', 'Status Code', 'Bytes', 'Url', 'User-agent'])
        for line in data:
            p= line.split(" ")
            #print(p)
            x = str(p[10][1:]) +str(p[11][:15])+str(p[6])
            wr.writerow([p[5][1:],p[8],p[9],x,p[12][1:]])
            #print("Method:",p[5][1:],"Status Code:",p[8],"bytes:",p[9],"Url:",x ,"user-agent:",p[12][1:])

f = open("abcd.txt", mode='r')
data = f.readlines()
for line in data:
    p = line.split(" ")
    #print(p)
    x = str(p[10][1:]) + str(p[11][:15]) + str(p[6])
    with open("datanew.csv", mode='a', newline='') as h:
        h.write("Method:"+p[5][1:]+"\t"+"Status Code:"+p[8]+"\t"+"bytes:"+p[9]+"\t"+"Url:"+x+"\t"+"user-agent:"+p[12][1:]+"\n")
f.close()

cCount = lCount = wCount = 0
with open("file.txt", mode='r') as f:
    data = f.readlines()
    for line in data:
        lCount +=1
        #print(len(line))
        cCount = cCount + len(line)
        words = line.split(" ")
        wCount = wCount+len(words)
f.close()
print("lCount:",lCount,"wCount:",wCount,"cCount:",cCount)


print("********Python Program to retrieve the count of letter in a File ********")
letter = input("Enter letter:")
k=0
with open("file.txt", mode='r') as f:
    data = f.readlines()
    for line in data:
        words = line.split(' ')
        for i in words:
            for l in i:
                if l.casefold() == letter.casefold():
                    k=k+1
    print(k)

print("********Python Program to Read the Contents of a File in Reverse Order********")
for line in reversed(list(open("file.txt"))):
    print(line.rstrip())

