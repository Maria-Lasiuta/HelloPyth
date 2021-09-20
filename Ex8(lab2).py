list1=['d','cccc','bb','aaa']

def mysort(mylist = [],numflag = False):
    if numflag == False:#
        list1.sort(key = lambda x: x[0])
    else:
        list1.sort(key = len)
    return print(list1)

mysort(list1)
mysort(list1, True)
print('DONE')
