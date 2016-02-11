#Insertion Sort. Best O(n) (nearly sorted) - worts/avg O(n^2)
import random

def sort(arr):
    for i in range(1, len(arr) ):
        val = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > val):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = val


a = []
for i in range(50):
    a.append(random.randint(1,100))
print a
sort(a)
print a
