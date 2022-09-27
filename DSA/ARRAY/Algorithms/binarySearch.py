# 1. Iteration Method
"""
binarySearch(arr,x,low,high):
    repeat till low == high
            mid = (low+high)/2
                if ( x == arr[mid])
                    return mid 
                else if (x > arr[mid]) // x is on the right side 
                    low = mid + 1
                else                // x is on the left side 
                    high = mid - 1
    """

def binarySearch(arr,x,N,low,high): 
    while low<=high:        
        mid = (low+high)//2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]<x):
            low = mid+1
        else:
            high = mid - 1
    return - 1
    
if __name__=="__main__":
    arr = [1,9,3,4,8,21]
    x = 3
    N = len(arr) 
    arr.sort()
    low = arr[0]
    high = N-1
    ans = binarySearch(arr,x,N,low,high)
    
    if(ans!=-1):
        print("Element ",x ," found at ", ans , " index ")
    else:
        print("Not Found ")