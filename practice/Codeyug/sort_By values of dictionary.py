my_list = [['Jay', 85], ['Viru', 80],['Basanti',95],['Thakur',83],['Sambha', 85]]
my_dict = dict(my_list)
m = set(my_dict.values())
marks = sorted(m)
max_marks = marks[-2]
print(max_marks)
for i in my_list:
    if i[1]==max_marks:
        print(i[0])
