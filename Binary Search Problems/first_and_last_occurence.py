# here we gonan find out the first and last occurence of an element

# 1. Brute force appraoch
def first_last_approach(arr,n,x):
    f = -1
    l = -1
    for i in range(n):
        if arr[i] == x:
            f = i
            break
    for j in range(f,n):
        if arr[j] == x:
            l = j
    return f,l


# Better appraoch




# optimal approch
# Here we gonna used Binary search algorithm to find out the first and last index of an element
# time complexity - 2*O(nlogn)
# spce complexity - O(1)

def  binary_search_left(arr, n, x):
    low = 0
    high = n - 1
    first = -1
    while(low <= high):
        mid = (low + high)//2
        if arr[mid] == x:
            first = mid
            high = mid - 1  # looks for small index on the left
        elif (arr[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return first

def  binary_search_right(arr, n, x):
    low = 0
    high = n - 1
    last = -1
    while(low <= high):
        mid = (low + high)//2
        if arr[mid] == x:
            last = mid
            low = mid + 1  # looks for large index on the right
        elif (arr[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return last


def first_last(arr,n,x):
    f = binary_search_left(arr,n,x)
    l = binary_search_right(arr,n,x)

    return (f,l)


arr = [1,2,3,3,3,3,4,5]
x = 3
n = len(arr)
print("first and last occurence of an element ")
print(first_last(arr,n,x))
