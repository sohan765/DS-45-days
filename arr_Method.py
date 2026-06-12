 l = [10,20,30,40,50,60,80,70]
import numpy as np
arr = np.array(l)
print(arr)
print(f"the sum of array is : {arr.sum()}")
print(f"the mean of the array is :{arr.mean()}")
print(f"The maximum and minimum element in array is : {arr.max()} and {arr.min()}")

arr1 = arr.reshape(2,4)
print(f"array reshape is : {arr1}")
print(np.sort(arr))
print(" array converted into 1D from 2D ",arr1.flatten())
print(arr.ndim)
print(arr.size)
print(arr.dtype)


FLATTEN USE TO CONVERT n D TO 1D 
arr = np.arange(12).reshape(3,4)
print(arr)
up_arr = arr.flatten() // create copy than work
print(up_arr)

arr1 = np.arange(24).reshape(2,3,4)
print(arr1)
up_new = arr1.flatten()
print(up_new)

ravel
arr2 = np.arange(18).reshape(7,2)
print(arr2)
up_new1 = arr2.ravel() # it work on original array
print(up_new1)

arr3 = np.arange(147).reshape(7,7,3)
print(arr3)
up_new2 = arr3.ravel()
print(up_new2)

arr3 = np.arange(24).reshape(4,3,2)
up_arr3 = arr3[0,0,0]
print(up_arr3)
up_arr3 = arr3[-1,-1,-1]
print(up_arr3)

arr = np.arange(12)
i=0
while i < len(arr):
    print(arr[i], end = " ")
    i += 1
arr = np.arange(24).reshape(6,4)
i = 0
while i < len(arr):
    j = 0
    while j < len(arr[i]):
        print(arr[i][j], end=" ")
        j += 1
    print()  # Move to the next line after each row
    i += 1   

arr = np.arange(12).reshape(2,2,3)
i=0
while i< len(arr):
    j=0
    while j < len(arr[i]):
        k = 0
        while k< len(arr[i][j]):
            print(arr[i][j][k],end = " ")
            k += 1
        print()
        j += 1
    i +=1

 2D ARRAY USING FOR LOOP
arr = np.arange(12).reshape(3,4)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print()
3D ARRAY USING FOR LOOP
arr = np.arange(12).reshape(2,2,3)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            print(arr[i][j][k], end = " ")
        print()

SORT 1D ARRAY 
arr = np.array([3,2,1,6,8,5,90,8])
arr_new = np.sort(arr)
print(arr_new)

arr1 = np.array([[4,2,3],[7,9,5]])
arr1_new = np.sort(arr1)
print(arr1_new)  # Default sorting row wise in 2d array in numpy
in case of row pass 1 and in case of column pass 0
Row --> 1
Column --> 0
arr1_new1 = np.sort(arr1,axis = 0)
print(arr1_new1)
arrc = np.sort(arr1)[:,::-1] # : → select all rows  
                             ::-1 → select columns from end to beginning (reverse order)
print(arrc)
filter 
arr = np.array([12,7,56,98,6,45,34])
print(arr)
arr_f = arr[arr<56]
print(arr_f)
arr_d = arr[arr%2==0]
print( arr_d)

filtering rows in 2d array
arr  = np.array([[2,5,3],[9,6,1]])
arr_r2 = arr[arr[:,0]>5] # for  rows
print(arr_r2)

column filtering 2d
arr_c2 = arr[:,arr[0,:]>1]
print(arr_c2)
 fancy indexing
arr = np.array([2,5,5,98,76,234])
arr1 = arr[[0,2]]
print(arr1)

arr = np.array([2,3,6,5,4,78,90])
arr_w = np.where(arr>20,"True","False")
print(arr_w)
