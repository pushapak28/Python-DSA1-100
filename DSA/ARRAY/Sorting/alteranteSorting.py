
def alternatesort(arr,n):
    arr.sort()
    
    print(arr)
    # Printing the last element of array
    # first and then first element and then
    # second last element and then second
    # element and so on.
    i = 0
    j = n-1
    
    while(i<j):
        print(arr[j],end = " ")
        j-=1
        print(arr[i],end = " ")
        i+=1
        
    # print(arr[i])
    # If the total element in array is odd
    # then print the last middle element.
    if(n%2!=0):
        print(arr[i])
    

arr = [1,12,4,6,7,10,3]
n = len(arr)

alternatesort(arr,n)