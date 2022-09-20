from array import array


array_num = array('i',[1,2,3,4])

array_num.extend(array_num)
print("extends ", str(array_num))