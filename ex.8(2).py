list1=['d', 'cccc', 'bb', 'aaa']

def mysort(mylist = [],numflag = False):
    if numflag == False:
        mylist.sort(key = lambda x: x[0])
    else:
        mylist.sort(key = len)
    return print(mylist)

mysort(list1)
mysort(list1, True)
print('DONE')
