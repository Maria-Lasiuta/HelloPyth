'''Question
Write a function that asks the user to enter a list of integers. Do the following:

Print the total number of items in the list.
Print the last item in the list.
Print the list in reverse order.
Print Yes if the list contains a 5 and No otherwise.
Print the number of fives in the list.
Remove the first and last items from the list, sort the remaining items, and print the result.
Print how many integers in the list are less than 5.'''
def lists(list_of_integer):
          print(len(list_of_integer))
          print(list_of_integer[-1])
          list_of_integer.reverse()
          print(list_of_integer)
          if '5' in list_of_integer:
              print('Yes')
          else:
              print('No')
          count = 0
          for i in list_of_integer:
              if i == '5':
                  count+=1
          print(count)
          list_of_integer[1:-1]
          list_of_integer.sort()
          print(list_of_integer)
          number=0
          for i in list_of_integer:
              if i < '5':
                  number+=1
          print(number)
list_of_integer  = list(input('Введіть список з цілих чисел: '))
lists(list_of_integer)           
