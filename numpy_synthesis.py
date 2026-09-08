import numpy as np

# 배열 생성
np_array01 = np.array([3,2,1])
np_array02 = np.zeros((2,3))
np_array03 = np.ones((3,3))
#np_array04 = np.arange(0,11,2)
np_array04 = np.arange(5)
array05 = np.linspace(0,1,4)

print(np_array01)
print(np_array02)
np_array02[1,1] = 9.0
print(np_array02, type(np_array02))
print(np_array03)
print(np_array04)
print(array05)