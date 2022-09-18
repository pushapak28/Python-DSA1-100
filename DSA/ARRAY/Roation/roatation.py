# 1 method 
# time complexity O(n)
# Auxiliary Space O(n)
"""
def rotate(L,d):
    k=L.index(d)
    print(k)
    new_Lis=[]
    new_Lis= L[k+1:]+L[0:k+1]
    print(L[k+1:])
    print(L[0:k+1])
    return new_Lis

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    d=2
    # Function Call
    arr = rotate(arr,d)
    print("rotatin array : ")
    for i in arr:
        print( i,end=" ")
        
    """

        
#  2 Method 
def rotationArray(L,d,n):
    p = 1
    while(p<=d):
        last = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = last
        p=p+1     
    
def printArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    
arr = [1,2,3,4,5,6,7,8]
d = 2 
N = len(arr)

rotationArray(arr,d,N)
printArray(arr,N)

# Time Compexity O(n*d)
# Auxiliary space O(1)

    