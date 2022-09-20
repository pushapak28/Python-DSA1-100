

from array import array


num_list = [1,2,3]
array_num = array('i',[])
print("List ", str(num_list))

array_num.fromlist(num_list)
print("Array ",str(array_num))

num_list1 = []
num_list1 = array_num.tolist()

print("List ",str(num_list1))



