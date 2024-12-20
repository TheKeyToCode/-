from random import randint
import time
start_time = time.time()

def  insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    return array
n = int(input("Enter the size of the array: "))

array = [randint(0, 100) for i in range(n)]
print(array)

print(insertion_sort(array))

end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time//0.001/1000, "seconds")

