from random import randint

def selection_sort(array):
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
print(selection_sort(array))
