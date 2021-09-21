#ex.3
#Generate a random number between 1 and 10. Ask the user to guess the
#number and print a message based on whether they get it right or not.

import random
x=random.randint(1,10)
y=int(input('Guess and enter the number: '))
def number(order):
  if x==y:
    print("you guessed it")
  else:
    print("you didn't guess(((")

number(y)
print('The correct number:',x)


        
