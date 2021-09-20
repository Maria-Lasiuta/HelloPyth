a=['d','cccc','bb','aaa']

def mysort(mylist=[],numflag=False):
    if numflag==False:
        a.sort(key=lambda x: x[0])
    else:
        a.sort(key=len)
    return print(a)
mysort(a)
mysort(a,True)
