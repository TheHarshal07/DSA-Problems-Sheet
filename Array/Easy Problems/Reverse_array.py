# Code for the reverser the array


# Time complexity - O(n)
# Space Complexity - O(1)

def Revers_array(arr,n):
    low = 0
    high = n-1

    while(low < high):
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high -= 1

    return arr

arr = [1,2,3,4,5]
n = len(arr)
print(Revers_array(arr,n))