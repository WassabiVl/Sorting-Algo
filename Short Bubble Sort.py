import time
start_time = time.time()
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
       passnum = passnum-1

alist=[93,54,26,62,17,77,31,44,55,20,10]
shortBubbleSort(alist)
print(alist)
print("--- %s seconds ---" % (time.time() - start_time))
#steps taken 314, time 0.0935356616973877 seconds