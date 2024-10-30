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

def  insertion_sort(array:list):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    return array
def selection_sort(A):
    for i in range(len(A) - 1):
        min_index = i
        for k in range(i + 1, len(A)):
            if A[k] < A[min_index]:
                min_index = k
        A[i], A[min_index] = A[min_index], A[i]
    return A
# def merge(left, right):


def merge_sort(array:list):
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

def quick_sort(array:list):
    if len(array) <= 1:
        return array
    else:
        mid = randint(0, len(array) - 1)
        part1 = array[:mid]
        part2 = array[mid:]
        part1 = quick_sort(part1)
        part2 = quick_sort(part2)
        return merge(part1, part2)
