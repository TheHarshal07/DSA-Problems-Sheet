# To find out the largest three element in the array
import sys
def largest_three_element(arr,n):
    Flarge = Slarge = Tlarge = -sys.maxsize-1
    for i in range(n):
        if arr[i] >= Flarge:
            Tlarge = Slarge
            Slarge = Flarge
            Flarge = arr[i]
        elif (arr[i]>Slarge):
            Slarge = Tlarge
            Slarge = arr[i]
        elif (arr[i] > Tlarge):
             Tlarge = arr[i]

    print("Three largest element are", Flarge,Slarge,Tlarge)

arr = [100,200,300,400,500]
largest_three_element(arr,len(arr))
