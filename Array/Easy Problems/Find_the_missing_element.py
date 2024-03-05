# Find out the missing element in the arary
'''
Methode - 1 By using sum of all naturals number
mehtode - 2 Using XOR methode ( which is slidely better than the methode 1 )

'''
def Missing_element(arr,n):
    res = 0
    sum = int(n*(n+1)/2)
    for i in range(n-1):
        res += arr[i]    
    ans = sum - res
    return ans

arr = [ 1,2,3,5,6,7]
n = len(arr)
print(Missing_element(arr,n))
