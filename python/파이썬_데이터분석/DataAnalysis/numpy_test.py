"""

넘파이에 대해서 

-> 수치 계산 라이브러리 

선형 대수 연산에 필요한 다차원 배열과 배열 연산을 수행하는 다양한 함수 제공 


numpy에서 배열은 ndarray , array라고 부른다. 

파이썬의 list 배열과 다르다. 

numpy : [ 10 , 11 ,12 ] + [ 1 , 2, 3 ]  = [ 11 , 13 , 15 ]

list : [ 10 , 11 ,12 ] + [ 1 , 2, 3 ] = [ 10, 11, 12, 1, 2, 3 ]



"""

import numpy as np

# a = np.arange(15).reshape(3,5)

# print(a.shape) 

# print(a.ndim)

# print(a.dtype) # 배열의 타입은 모두 동일하다. 즉, int 원소가 있으면 배열 전체의 원소 타입이 int 
 
# print(a.itemsize)

# print(a.size) # 전체 요소 개수 


"""

numpy 배열 생성 

np.zeros , np.ones , np.empty를 이용하여 다양한 차원의 데이터를 쉽게 생성이 가능하다. 

np.zeros(shape) : 0으로 구성된 n차원 배열 생성 -> 배열 초기화에 좋다. 

* np.array를 이용하여 파이썬에서 사용하는 튜플이나 리스트를 입력으로 nu,py.ndarray를 생성



"""

# 배열 생성 

# array_test = np.array([2,3,4])

# print(array_test)

# print(array_test.dtype)

# print(array_test.size)

# print(array_test.shape)


# np_zeros = np.zeros([3,4])

# print(np_zeros)

# np_ones = np.ones((5,5))

# print(np_ones)

# array_test3 = np.arange(7).reshape(1,7)

# print(array_test3)

# empty = np.empty([4,5,3], dtype=int)

# print(empty)

"""

넘파이 연산 

numpy(A@B) -> 행렬곱 



"""


# random_array = np.empty([5,100])

# random_array = np.random.randint(0,50,(2,25)) # 0 ~ 50까지 ( 2행 25열 배열 생성 )

# random_array = np.arange(15).reshape(3,5)

# print(random_array.max()) # 가장 높은 숫자 

# print(random_array.argmax()) # 가장 높은 숫자의 인덱스 

# print(random_array.sum())

# print(random_array.cumsum()) # 모든 요소의 누적합 


# 0 ~ 7까지 숫자를 2행 4열로 만들고, 해당 원소의 값에 제곱을 수행 

a = np.arange(8).reshape(2,4)**2 

# print(a)

# print(a.sum())

# print(a.min())

# print(a.argmax())

# print(a.cumsum())

# print(a.dtype)

# print(a.sum(axis=0)) # 열기준 원소 합 연산 -> 열이 4열이므로, 4개의 원소 출력

# print(a.sum(axis=1)) # 행 기준 원소 합 연산 -> 행이 2개이므로, 2개의 원소 출력 

# print(a.max(axis=1)) # 각 행에서 가장 큰 숫자 출력 

# b = np.array([1,4,9])

# print(np.sqrt(b))

"""

넘파이 인덱싱과 슬라이싱 

"""

# a = np.arange(8)**2


# i = np.array([1,1,3,5])

# i = [ 1, 1, 3, 5]

# z = [[1,1],[3,5]]

# print(z)

# print(a[i])

# print(a[z])


# a = np.arange(12).reshape(3,4)

# print(a)

# b = a > 4 # 4 보다 큰 값을 Ture 

# print(b) 

# print(a[b]) # 4보다 큰 값들만 1차원 배열로 출력된다. 

# print(a[b].shape) # 4보다 큰 값들의 1차원 배열 형태 -> 7, 로 출력 

# a[b] = 0 # True인 값에 0을 대입한다. 

# print(a)


### 복습 


# a = np.zeros(15).reshape(3,5)


# print(a.shape[0])

# for i in range(a.shape[0]):
#     if i > 1 :
#         a[i] = 1
# print(a)

# a = np.arange(15).reshape(3, 5)

# # Set all elements in the array to 1 where the condition is True
# a[a > 5] = 1

# print(a)

## 넘파이 크기 변경 

# a = np.arange(12).reshape(3,4)

# print(f" 배열 : {a}")


# print(f"2차원 -> 1차원 : {a.reshape(-1)}")


# print(f"3,4 배열을 2,6으로 변환 {a.reshape(2,6)}")


# print(f"전치행렬 \n{a.T}")

# print(f"전치행렬 \n{a.T.shape}")

## 넘파이 데이터 합치기 


# a = np.array([0,1,2,3]).reshape(2,2)

# b = np.array([7,8,9,10]).reshape(2,2)

# print(np.vstack((a,b)))

# print(np.hstack((a,b)))

# a = np.arange(12).reshape(2,6)


# print(f"행을 기준으로 데이터를 3등분으로 분할 /n {np.hsplit(a,3)}")


# print(np.hsplit(a,(2,5))) # 3번째 열부터 4번째 열 미만을 기준으로 분할 

a = np.linspace(0,1,3)

print(a)