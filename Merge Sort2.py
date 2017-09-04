import time
start_time = time.time()
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    left = merge_sort(seq[:len(seq) // 2])
    right = merge_sort(seq[len(seq) // 2:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_count = 0
    right_count = 0
    try:
        while True:
            if left[left_count] > right[right_count]:
                result.append(right[right_count])
                right_count += 1
            else:
                result.append(left[left_count])
                left_count += 1
    except:
        return result + left[left_count:] + right[right_count:]

alist = [93,54,26,62,17,77,31,44,55,20,10]
merge_sort(alist)
print(alist)
print("--- %s seconds ---" % (time.time() - start_time))