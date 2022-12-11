my_dict = {'orange':'fruit', 'potato':'vegetable', 'banana':'fruit'}

output = {}
for ele in my_dict:
    if my_dict[ele] not in output:
        output[my_dict[ele]]=[ele]
    else:
        output[my_dict[ele]].append(ele)


print(output)


