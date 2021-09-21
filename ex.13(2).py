#Write a function that removes empty strings from the list of strings.
x = ['','abc','jnb']


def mlist(list1):
   y = []
   for string in x:
     if (string !=''):
        y.append(string)
   return print(y)

mlist(x)

