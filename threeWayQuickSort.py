#Three way quick sort (arguable the easiest way to implemnt + best w/ multiple elements) 
#see http://algs4.cs.princeton.edu/23quicksort/

import random

def swap(arr,i,j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def sort(arr, left, right):
    if right <= left: #IMPORTARNT! I was forgetting this
        return
    lt = left #Uses first ele as partition. Not optimal but easy and "good enough". Other methods include "median of 3" and median of medians.
    gt = right
    i = left
    while (i < gt):
        if arr[i] < arr[lt]:
            swap(arr, i, lt)
            i += 1 
            lt += 1 
        elif arr[i] > arr[lt]:
            swap(arr, i , gt)
            gt -= 1
        elif arr[i] == arr[lt]:
            i +=1
    sort(arr, left, lt-1) #recursivly calling itself to solve
    sort(arr, gt+1, right)

a = []
for i in range(50):
    a.append(random.randint(1,100))

print a
sort(a, 0, len(a) -1)
print a
