my_str = str(input('Введіть текст або числа,які має містити список :'))
a = list(my_str)
print(a)#список,який ми перевіряємо
def is_sorted(x, key = lambda x: x):
    return all([key(x[i]) <= key(x[i + 1]) for i in range(len(x) - 1)])
#all-повертає True or False
print(is_sorted(a))

