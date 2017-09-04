import time
start_time = time.time()
def mergeSort(array):
    if len(array) <= 1:
        return array
    else:
        left = array[:int(len(array)/2)]
        right = array[int(len(array)/2):]
        return merge(mergeSort(left),mergeSort(right))

def merge(array1, array2):
    merged_array = []
    pointer1, pointer2 = 0, 0
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            merged_array.append(array1[pointer1])
            pointer1 += 1
        else:
            merged_array.append(array2[pointer2])
            pointer2 += 1
    while pointer1 < len(array1):
        merged_array.append(array1[pointer1])
        pointer1 += 1

    while pointer2 < len(array2):
        merged_array.append(array2[pointer2])
        pointer2 += 1

    return merged_array
alist = [93,54,26,62,17,77,31,44,55,20,10]
mergeSort(alist)
print(alist)
print("--- %s seconds ---" % (time.time() - start_time))