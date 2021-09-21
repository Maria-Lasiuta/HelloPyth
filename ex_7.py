my_str = str(input('Введіть список :'))
my_list = list(my_str)
temp_list = []
for i in my_list:
    if i not in temp_list:
        temp_list.append(i)
my_list = temp_list
print(my_list)
