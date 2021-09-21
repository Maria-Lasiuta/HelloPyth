#4

item = int(input('How many items are you buying?:'))

if item<10 and item>0:
    print(item*12,'$')

if item >=10 and item <=99:
    print(item*10,'$')

if item >=9100:
    print(item*7, '$')
          
