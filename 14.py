#14
def sumDigits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum   

num = int(input('Enter a 4-digit number:'))
print('Sum of the digits:', sumDigits(num))

