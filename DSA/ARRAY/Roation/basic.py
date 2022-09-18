# import array
from array import *


# array used 
arr = array.array('i',[1, 2, 3])
print("The new created array: ",end=" ")

for i in range(0,3):
    print(arr[i],end=" ")
print("\r")

#  append use 

arr.append(4)

print("The appended array is :",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")
print("\r")


# insert function use 

arr.insert(2,5)
print("The insert array is: ",end=" " )
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")


# pop function use 
arr.pop(2)
# remover function use 
arr.remove(3)
print("The array after pop is : ",end=" ")
for i in  range(0,3):
    print(arr[i],end=" ")
print("\r")


# index function used 
print("Array after used index function: ",arr.index(1))


# rervse function
arr.reverse()
print(arr)

# array type
print("array type: ",arr.typecode)

# array size 

print("Array size: ",arr.itemsize)

print("buffer info of array: ",arr.buffer_info)


