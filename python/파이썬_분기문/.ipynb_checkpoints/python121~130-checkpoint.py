"""
주민 번호 유효성 검사 

주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 
먼저 앞에서 부터 12자리의 숫자에 2,3,4,5,6,7,8,9,2,3,4,5를 차례로 곱한 뒤 그 값을 전부 더하고, 
연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록 번호의 마지막 값이 된다. 
"""

# nums = input("주민번호를 입력하세요. 12자리 (하이픈 포함) : ")

# # 하이픈을 기준으로 주민번호를 분리
# first_number, second_number = nums.split("-")

# # 하이픈을 제거하고 주민번호를 합침
# full_number = list(first_number + second_number)

# print(full_number)

# multiple_num = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# # 결과를 저장할 리스트 초기화
# numbers = []

# # full_number의 각 자릿수를 순회
# for i in range(0, len(full_number)):
#     # 각 자릿수를 정수로 변환
#     numbers.append(int(full_number[i]) * multiple_num[i])

# last_num = 11 - sum(numbers) % 11

# identity_number = nums + str(last_num)


# print(identity_number)

## 5/20 #############
