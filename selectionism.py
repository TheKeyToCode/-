from random import randint
import time

from quick_sort import check

start_time = time.time()
def selection_sort(A):
    for i in range(len(A) - 1):
        min_index = i
        for k in range(i + 1, len(A)):
            if A[k] < A[min_index]:
                min_index = k
        A[i], A[min_index] = A[min_index], A[i]
    return A

n = int(input("Enter the size of the array: "))
array = [randint(0, 100) for i in range(n)]
print(array)
print(selection_sort(array))

end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time//0.001/1000, "seconds")
check(array)