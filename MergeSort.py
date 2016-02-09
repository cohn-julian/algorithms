#Merge sort - a very good sorting algo that has O(n lgn) for all running times. It has a higher space cost then quicksort causing it to be overlooked but it is very easy to explain/write for how powerfull it is.
#NOT WORKING - numbers are changing....


import random
def merge_sort(arr,aux, low, high):
    if high <= low:
        return
    if len(arr) > 1:
        middle = low  + (high-low)/2
        merge_sort(arr, aux, low, middle)
        merge_sort(arr, aux, middle+1, high)
        merge(arr, aux, low, middle, high)
def merge(arr, aux, low, middle, high):
    left_li = []
    left_li.extend(arr[low : middle+1])
    right_li = []
    right_li.extend(arr[middle+1: high+1])
    left_li.append(2147483647)
    right_li.append(2147483647)
    i = 0
    j = 0
    for k in range(low, high+1):
        if left_li[i] <= right_li[j]:
            arr[k] = left_li[i]
            i += 1
        else:
            arr[k] = right_li[j]
            j += 1

def test():
    auxi = []
    arrr = []
    for i in range(10):
        arrr.append(random.randint(1,1000))
    print arrr
    merge_sort(arrr, auxi, 0, len(arrr) -1)
    print arrr

test()
