from random import randint
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    # return array

def  insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    # return array
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
def quick_sort(array: list):
    if len(array) <= 1 or array.count(array[0]) == len(array):
        return array
    else:
        rand = randint(0, len(array) - 1)
        key = array[rand]
        l = 0
        r = len(array) - 1
        while l <= r:
            if array[l] >= key:
                if array[r] < key:
                    array[l], array[r] = array[r], array[l]
                    l+=1
                r-=1
            else:
                l+=1
        answer = quick_sort(array[:l])
        answer.extend(quick_sort(array[l:]))
        array[:] = answer[:]
        return answer
def selection_sort(A):
    for i in range(len(A) - 1):
        min_index = i
        for k in range(i + 1, len(A)):
            if A[k] < A[min_index]:
                min_index = k
        A[i], A[min_index] = A[min_index], A[i]
    # return A
