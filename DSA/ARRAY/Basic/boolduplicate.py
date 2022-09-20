
def test_duplicate(arr):
    
    new_arr = set(arr)
    return len(arr) != len(new_arr)

print(test_duplicate([1,2,3,1,2]))
print(test_duplicate([1,2,3,4]))