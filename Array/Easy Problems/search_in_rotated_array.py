# Here we have search in rotated  array

def Search_in_rotated_array(arr,n,k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

arr = [1,2,3,4,5]
k = 3
print(Search_in_rotated_array(arr,len(arr),k))