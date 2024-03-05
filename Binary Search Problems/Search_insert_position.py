# Here we gonna write a search in insertion position
# if the element present in the array then we have to return the index of that element and
# if it is not present then we have to return right postition  where we can insert that element


#Apprach would be the Binary search algorithm

def searchInposition(arr,n,m):
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low + high)//2
        if arr[mid] <= m:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans



arr = [1,2,4,7]
n = len(arr)
m = 6
print(searchInposition(arr,n,m))
