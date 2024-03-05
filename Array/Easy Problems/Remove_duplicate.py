# Code to remove the duplicates
# Time Complexity - O(n)
# Space complexity - O(n)
def RemoveDuplicates(arr,n):
    s = set()
    for i in range(n):
        s.add(arr[i])
    return s

arr = [1,2,2,3,3,4,5,5]
print(RemoveDuplicates(arr,len(arr)))