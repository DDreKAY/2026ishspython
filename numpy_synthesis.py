import numpy as np

# 배열 생성
np_array01 = np.array([3,2,1])
np_array02 = np.zeros((2,3))
np_array03 = np.ones((3,3))
#np_array04 = np.arange(0,11,2)
np_array04 = np.arange(5)
array05 = np.linspace(0,1,5)

# 배열 속성 (attribute)
print(np_array01.shape) #배열 모양 (행, 열, (면))
print(np_array02.shape)
print(np_array03.ndim) # 차원수
print(np_array04.dtype) #데이터 타입
print(array05.size) #전체 원소 개수