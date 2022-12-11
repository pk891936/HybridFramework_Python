import json

with open('../testCases/sample_file.json', 'r') as f:
    data = json.load(f)

data['first_name'] = 'JSON!'

with open('../testCases/sample_file.json', 'w') as f:
    json.dump(data, f, indent=2)
    print("File dict modified")


a=[1,2,3,4]
b=[2,3,6,1]
for i in a:
   for j in b:
       if i==j:
           print(i)

x = [i for i in a if i in b]
print(x)
