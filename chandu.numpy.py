import numpy as np
#array=np.array([20,40,60,80,100])
#array1=array.copy()
#print(array1)
#array1[2]=1786
#print(array)
#print(array1)


"""array=np.array([1,2,3,4,5,6])
array2=array.view()
#print(array2)
array2[3]=1234
print(array)
print(array2)
print(array.shape)"""


"""arr=np.array([1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77])
arr1=arr.reshape(4,4)
print(arr1)"""

#FOR 3D
'''arr=np.array([1,2,3,4,5,6,7,8,9,12,12,23])
arr1=arr.reshape(2,3,2)
print(arr1)'''

#any dimensional to 1D
'''arr=np.array([[12,2,35],[67,86,34],[96,23,41]])
arr1=arr.reshape(-1)
print(arr1)'''

'''arr2=np.array([[['Ammu','varuun','vamshi','vijay'],['anjali','akshay','anamika','arun'],['vageshh','arjun','sunny','anjali']]])
arr3=arr2.reshape(-1)
print(arr3)
            '''
'''arr1=np.array([12,34,45])
for i in arr1:
    print(i)
'''
'''arr=np.array([[[1,2,3],[4,5,6],[6,9,3]]])
for i in arr:
    print(i)'''

#enumerate
'''arr=np.array([[12,23],[45,89]])
for index,value in np.ndenumerate(arr):
    print(index,value)'''

'''
arr=np.array([[12,23],[45,89]])
for idx,i in np.ndenumerate(arr):
    print(idx,i)'''
'''ar1=np.array([1,2,3,4,5])
ar2=np.array([23,24,25,26,27])
ar3=np.array([31,32,33,34,35])
arr=np.concatenate((ar1,ar2,ar3))
print(arr)'''

'''ar1=np.array([[1,2,3],[34,35,36]])
ar2=np.array([[23,24,25],[67,68,69]])
ar3=np.array([[31,32,33],[98,96,97]])
arr=np.concatenate((ar1,ar2,ar3),axis=1)
print(arr)'''
'''arr1 = np.array([1,2,3,4,5])
arr2 = np.array([7,5,9,7,8])
arr3 = np.array([5,7,8,9,9])
arr = np.stack((arr1,arr2,arr3), axis=2)
arr'''

'''arr1=np.where(arr>2)
print(arr1)'''

'''arr2=np.array([23,34,56,67,78,89,23,45,65,43,11,23,45,23,23])
x=np.where((arr2==45)&(arr2==23))
print(x)'''

#arr=np.array([10,20,30,40,50])
#result=np.where((arr>20) &(arr<50))
#print(result)                


'''arr=np.array([1,2,3,5,6,7])
arr1=np.searchsorted(arr,67)
print(arr1)

arr1=np.array([1,2,3,5,6,7])
arr11=np.searchsorted(arr1,4)
print(arr11)

arr3=np.array([1,2,3,5,6,7])
arr4=np.searchsorted(arr3,7, side='left')
print(arr4)

arr3=np.array([1,2,3,5,6,7,8,9])
arr4=np.searchsorted(arr3,7, side='right')
print(arr4)'''
'''arr=np.array([1,2,3,4,5,6])
arr1=np.sort(arr)
print(arr1)

arr=np.array([1,2,3,4,5,6])
arr1=np.sort((arr)[::-1])
print(arr1)


arr=np.array([1,2,3,4,5,6])
arr1=-np.sort(-arr)
print(arr1)'''


'''arr=np.array([12,34,56,78,43])
ar11=np.where(arr>34)
print(ar11)
'''

arr=np.array([1,2,3,4,56,7,89])
new_array=[]
for elment in arr:
    if element>34:
        new_array.append(True)
    else:
        new_array.append(False)
array1=arr[new_array]
print(array1)
print(new_array)
        
         

      
