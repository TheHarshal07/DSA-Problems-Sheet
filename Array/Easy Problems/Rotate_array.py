#Code for rotate the array 

# Rotate the array to the left
def Roata_left(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr


# Rotate the arry to the right
def Rotate_right(arr,n):
    temp1 = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp1
    return arr


# Roatate the array by k 
# Time Complexity - O(n)
def  Rotate_by_k(arr,n,k):
    for i in range(k):
        temp = arr[n-1]
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = temp
    return arr


#Optimal approch
# TIme complexity - 

def Optimise_Roatation(arr,low,high):
    while(low < high):
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low += 1
        high -= 1
    return arr
arr = [2,3,4,5,6]
n = len(arr)
k = 2

Optimise_Roatation(arr,0,n-k-1)
Optimise_Roatation(arr,n-k,n-1)
print(Optimise_Roatation(arr,0,n-1))


# print(Roata_left(arr,n))
print(" ")
# print(Rotate_right(arr,n))
print("")
k = 2
# print(Rotate_by_k(arr,n,k))
