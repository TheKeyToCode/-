from heapq import merge
from random import randint
import time
from code_to_check import check
start_time = time.time()

# def merge(arr):


def merge (left, right):
    # print(left, right)
    answer = []
    l = 0
    r = 0
    while l<len(left) and r < len(right):
        if left[l] <= right[r]:
            answer.append(left[l])
            l += 1
        else:
            answer.append(right[r])
            r += 1
    if(l!=len(left)):
        answer.extend(left[l:])
    if (r != len(right)):
        answer.extend(right[r:])

    # print(answer)
    return answer

def merge_sort(array):
    if(len(array)<=1):
        return array
    left = array[:len(array) // 2]
    right = array[(len(array)) // 2:]
    # print(left, right)
    left = merge_sort(left)
    right = merge_sort(right)
    # print(left,right)
    array[:] = merge(left, right)[:]
    # print(array)
    return array



n = int(input("Enter the size of the array: "))
array = [randint(0, 100) for i in range(n)]
print(array)
merge_sort(array)
print("Array: ", array)


end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time//0.001/1000, "seconds")

print(check(array))