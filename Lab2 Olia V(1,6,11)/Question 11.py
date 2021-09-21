'''Question 11
Write a function that reverse the tuple.'''

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
tuples = (10, 'Hello', (1, 2, 3), 3.14)
print(reverse(tuples))
