n = int(input("How many credits you have taken? "))
if n <= 23:
    print('You are a freshman')
elif n >= 24 and n <= 53:
    print('You are a sophomore')
elif n >= 54 and n <= 83:
    print('You are a junior')
elif n >= 84:
    print('You are a senior')
    
