my_list = [1,1,2,3,4,3,0,0]
temp_list = []
for i in my_list:
    if i not in temp_list:
        temp_list.append(i)
my_list = temp_list
print(my_list)
