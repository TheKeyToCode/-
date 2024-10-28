from heapq import merge
from random import randint

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

n = int(input("Enter the size of the array: "))
array = [randint(0, 100) for i in range(n)]
print(bubble_sort(array))
print(array)

def  insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    return array
def selection_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    return array
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        o = merge(left, right)
        print(merge(array,left, mid , right))
        return merge(array, left, right)
    return array

array = [randint(0, 100) for i in range(n)]
print(insertion_sort(array))
print(array)
array = [randint(0, 100) for i in range(n)]
print(selection_sort(array))
print(array)
print(merge)
print("m")
array = [randint(0, 100) for i in range(n)]
print(merge_sort(array))
print(array)

