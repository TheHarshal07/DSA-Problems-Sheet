#Here we gonna find the ceil and floor round element present in the array

def ceilRound(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while(low <= high):
        mid = (low + high)//2
        if arr[mid] >= x: # This for ceil round
            ans = arr[mid]
            high = mid -1
        else:
            low = mid + 1
    return ans

def floorRound(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while(low <= high):
        mid = (low + high)//2
        if arr[mid] <= x: #This is for floor round
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid -1
    return ans


def floorAndceil(arr,n,x):
    ceil = ceilRound(arr,n,x)
    floor = floorRound(arr,n,x)

    return (ceil, floor)

arr=[10,20,30,40,50]
x = 25
n = len(arr)
print(floorAndceil(arr,n,x))