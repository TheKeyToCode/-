from random import randint
import time
from code_to_check import check
start_time = time.time()

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
n = int(input("Enter the size of the array: "))
array = [randint(0, 100) for i in range(n)]
print(array)
quick_sort(array)
print(array)
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time//0.001/1000, "seconds")

print(check(array))