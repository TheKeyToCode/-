from heapq import merge
from random import randint
import time
from code_to_check import check
start_time = time.time()

def quick_sort(array: list):
    if len(array) <= 1 or array.count(array[0]) == len(array):
        # if len(array)>1 and array.count(array[0]) == len(array):
        #     print("YEEEEEE: ", array)
        return array
    else:
        rand = randint(0, len(array) - 1)
        key = array[rand]
        l = 0
        r = len(array) - 1
        while l <= r:
            # print(l, r)
            if array[l] >= key:
                if array[r] < key:
                    array[l], array[r] = array[r], array[l]
                    # print(array)
                    l+=1
                r-=1
            else:
                l+=1

        # if(l==r):
        #     l+=1
        # print(array, l,  array[:l], r, array[l:], key)
        # print(l,r)
        answer = quick_sort(array[:l])
        answer.extend(quick_sort(array[l:]))
        # print(answer)
        array[:] = answer[:]
        return answer

        # return quick_sort(array[:r]).extend(quick_sort(array[r+1:]))


n = int(input("Enter the size of the array: "))
array = [randint(0, 100) for i in range(n)]
print(array)
quick_sort(array)
print(array)
# array = [70, 64, 84, 31, 30, 28, 11, 10, 97, 60]
# print(array)
# quick_sort(array)
# print(array)
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time//0.001/1000, "seconds")

print(check(array))