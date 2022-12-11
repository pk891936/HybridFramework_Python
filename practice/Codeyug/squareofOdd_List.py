l = [i for i in range(1,int(input('Enter range:')))]
#input = [1,2,3,4]
#output: [1,9]

output = [i*i for i in l if i%2!=0]
print(output)

print('***********Sum of remaining list***************')
input = [1,2,3,4]
output = []

output.append(input[0])
s = input[1:]
output.append(sum(s))
print(output)

