from random import randint
import time

from code_to_check import check

start_time = time.time()

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

n = int(input("Enter the size of the array: "))
array = [randint(0, 100) for i in range(n)]
print(array)
print(bubble_sort(array))
print(check(array))
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time//0.001/1000, "seconds")
