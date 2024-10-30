
def check1(arr):
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return False
    return True
def check2(arr):
    for i in range(len(arr)-1):
        if(arr[i]<arr[i+1]):
            return False
    return True
def check(arr):
    if(check1(arr) or check2(arr)):
        return True
