import time
start_time = time.time()
def shortBubbleSort(alist):
	passnum = len(alist)-1
	for i in range(passnum):
		if alist[i]>alist[i+1]:
			temp = alist[i]
			alist[i] = alist[i+1]
			alist[i+1] = temp
	for i in reversed(range(0,passnum-1)):
		if alist[i]>alist[i+1]:
			temp = alist[i+1]
			alist[i+1] = alist[i]
			alist[i] = temp
	for index in range(2,len(alist)-1):
		currentvalue = alist[index]
		position = index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1
		alist[position]=currentvalue
	   
alist=[93,54,26,62,17,77,31,44,55,20,10]
shortBubbleSort(alist)
print(alist)
print("--- %s seconds ---" % (time.time() - start_time))
 #steps taken 133, time 0.039132118225097656 seconds