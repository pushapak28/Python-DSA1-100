# 1 method 

# def linear_search(arr,x,N):
    
#     for i in range(N):
#        if x==arr[i]:
#            return True 
#     return False
        
# if __name__=="__main__":
#     arr = [1,2,3,4,8,21]
#     x = 3
#     N = len(arr)   
#     print(linear_search(arr,x,N))
    
#  2 method 

def linear_search(arr,x,N):
    if(N==0):
        return -1
    elif(arr[N-1]==x):
        return N-1
    else:
        return linear_search(arr,x,N-1)
    
if __name__=="__main__":
    arr = [1,2,3,4,8,21]
    x = 3
    N = len(arr)   
    ans = linear_search(arr,x,N)
    
    if(ans!=-1):
        print("Element ",x ," found at ", ans , " index ")
    else:
        print("Not Found ")
