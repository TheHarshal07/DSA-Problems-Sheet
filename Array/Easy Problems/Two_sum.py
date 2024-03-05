# Here we will gonna find the sum of the two elements

def two_sum(arr,n,target):
    stack = {}
    for i in range(n):
        diff = target - arr[i]
        if diff in stack:
            return [stack[diff],i]
        stacky[arr[i]] = i

    return []

arr = [6,1,4,3,6,8]
target = 7
print(two_sum(arr,len(arr),target))

