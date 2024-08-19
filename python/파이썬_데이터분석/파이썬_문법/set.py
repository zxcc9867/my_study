"""

집합 자료형 

중복을 허용하지 않는다. 

비순서 자료형 

순서를 사용하고 싶다면 리스트나 튜플로 변환하여 사용 

1. add 
2. update
3. remove

"""

# set1 = (set[1,2,3])

# print(set1)

# set2 = set("seettt")


# set1 = {1,2,3,4,5}

# set2 = {1,3,5,7,9}


# # 합집합 출력

# print(set1 | set2)

# # 교집합

# print( set1 & set2 )

# # 차집합

# print(set1 - set2 )

# print(set2 - set1)


"""
집합 함수 사용 
"""

set2 = {
    1,
    2,
    3,
    4,
    5,
}

set2.update([6, 7])  # 여러개의 값을 추가

print(set2)

set2.remove(6)

print(set2)
