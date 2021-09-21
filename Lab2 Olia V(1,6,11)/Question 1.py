'''Question 1
Write a program that asks the user to enter a length in centimeters.
If the user enters a negative length, the program should tell the user that
the entry is invalid. Otherwise, the program should convert the length to
inches and print out the result. There are 2.54 centimeters in an inch.'''
length = float(input('Введіть довжину в см: '))
if length < 0:
    print('Запис невірний')
else:
    length = length / 2.54
    print(length)
    
