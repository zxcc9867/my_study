"""

튜플은 괄호로 둘러싸인 자료구조 


보통은 2개의 원소만을 가진다. 하지만 2개 이상도 가능

-> 2개의 원소를 가지는 만큼, 2가지 정보를 사용하는 경우 

ex . ) 좌표 ( x, y ), 순서 저장 
"""

"""
딕셔너리 

-> 키 , 값을 가진다. 
-> 중괄호 
-> 각 키 벨류 원소는 콤마로 나누어져있다. 

dict = {}
"""

dict = {}

dict["a"] = ["add", "asign"]

dict_example = {"a": ["apple", "ant", "aunt"], "b": ["bee", "best", "brother"]}

"""
세트 -> 키만 있는 딕셔너리 

* 중복되는 원소가 존재할 수 없다. 
* 특정 원소가 세트안에 있는지 확인하는데 시간이 적게 든다. 
* 원래는 ant이라는 단어를 리스트에서 찾고자 할 때, 리스트의 하나하나의 값에 대해서 
매치를 해보고 찾아야하지만, set의 경우, 검색으로 ant가 있는지 한번에 찾아낼 수 있다.

"""

# 세트를 코드에서 활용하는 방법

# 비어 있는 상태로 선언
# 사전값을 하드코딩하여 대입

# exm =set()

# exm = {'ant','apple'}  #세트 상태로 선언

# exm.add('appeal')

# exm.remove('ant')

# print("apple" in exm)
# "all" in exm

""" 
반복문 -> 특정 코드를 특정 횟수만큼 반복하는 코드 
"""

"""
함수 
"""


# def arr_product(int_arr:int): # 이렇게 타입을 지정해줄 수 도 있다.
#     product = 1
#     return product + int_arr

# print(arr_product(2))

"""
파라미터 : 함수에 정의된 변수의 이름 

아규먼트 : 함수로 들어가는 값이 있는 변수
"""

"""
재귀함수 

자기 자신을 부르는 함수 

-> ex. ) 피보나치 수열의 n번째 숫자값을 구하기 

재귀함수는 큰 문제를 풀기 위해 작은 문제의 답을 사용해야할 때 

-> 동적 프로그래밍 

"""

# n = int(input('숫자를 입력하세요.'))

# def find_fibb(n: int):
#     if n <= 1:
#         return 1
#     else:
#         find_fibb(n-1) + find_fibb(n-2)
#         return find_fibb

"""
배열과 중첩 루프 

파이썬은 배열끼리 원소 타입이 다르거나 타입이 달라도 사용가능 

ex.) 2d_array = [[1,2,3,4,5], [6,7,8]]

ex.) 2d_array2 = [[1,2,3,4,5], ["a","b","c"]]

"""

number_of_seats = 3

seat_array = ["John", "jake", "James", "Amy", "Andy", "Alice"]

for i in range(len(seat_array)):
    if seat_array[i] == "Andy":
        andy_row_num = (i // number_of_seats) + 1
        andy_seat_num = (i % number_of_seats) + 1

seat_array2 = [["J", "b", "c"], ["a,b,c"]]

for i in range(len(seat_array2)):
    print(i)
