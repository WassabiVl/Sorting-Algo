def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       for i in reversed(range(passnum)):
           if alist[i]<alist[i+1]:
               exchanges = True
               temp = alist[i+1]
               alist[i+1] = alist[i]
               alist[i] = temp	
       passnum = passnum-1
	   
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)