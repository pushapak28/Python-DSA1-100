def find_duplicate(nums):
    num_set = set()
    no_duplicate = -1
    
    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])
        
    return no_duplicate
print(find_duplicate([1,2,3,1,3,5]))
print(find_duplicate([1,2,3,3,5]))


        
        
    