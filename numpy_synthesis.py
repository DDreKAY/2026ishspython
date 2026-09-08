import numpy as np

array01 = np.ones((3,4))
array02 = np.array([[1,2,3,10],[4,5,6,11],[7,8,9,12]])

print(array01)
array01[0,0] = 7.0

print(array01+array02)
array01=array01.T
array01=array01.reshape(6,2)
array02=array02.reshape(2,6)
print(array01 + 4.1)
print(np.sum(array01))
print(np.max(array01))
print(np.min(array02))
print(array01@array02)
array03=array01@array02
print(array03.flatten())

array03 = np.arange(1,11,1)
array04 = np.linspace(0,1,10)
print(array04.dtype)