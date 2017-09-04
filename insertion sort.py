import time
start_time = time.time()
def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1
		alist[position]=currentvalue

alist = [93,54,26,62,17,77,31,44,55,20,10]
insertionSort(alist)
print(alist)
print("--- %s seconds ---" % (time.time() - start_time))
#steps taken 110, time 0.02729487419128418 seconds