class Solution:
    def duplicates(self, arr, n):
        flags = False     
        array_dict = {}
        repeating_arr = []
        # loop through array and add to dictionary with the number of times it repeats 
        for a in arr:
            if a not in array_dict:
                array_dict[a] = 1
            else:
                array_dict[a] += 1
     # loop dictionary and append all repeating values to repeating array      
        for j in array_dict:
            if array_dict[j] > 1:
                flags = True
                repeating_arr.append(j)
     
     
        repeating_arr.sort()
     
     # if there is a flag for repeating character return [-1] or return sorted array
        if not flags: return [-1]
        return repeating_arr    

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        res = Solution.duplicates(arr,n)
        for i in res:
            print(i,end=" ")
        print()
        
                   
    