## 5월 6일 ##

"""
5월 6일 파이썬 문법 정리 시작 
"""

## type 함수

# a = 128

# print(type(a))

"""
문자열을 정수로 변환 
"""

# num_str = "720"

# result = int(num_str)
# print(type(result))

"""
에어컨이 월 48000원에 무이자 36개월을 조건으로 홈쇼핑에서 판매되고 있다. 총 금액을 계산한 후 이를 화면에 출력해보아라.
"""

# air = 48000 * 36

# print(air)

"""
문자열 인덱싱 
"""

## 1

# letters = "python"

# a = letters[0]+letters[2]

# print(a)

## 2

# list_plate = "24가 2210"

# print(list_plate[-4:])

"""
>> string = "홀짝홀짝홀짝" -> 홀만 출력하기 
"""
# string = "홀짝홀짝홀짝"

# # 방법 1
# result = ""
# for i in string:
#     if i == "홀":
#         result+=i
# print(result)

# # 방법 2

# print(string[::2])

"""
문자열을 거꾸로 출력하시오. 
>> string = "PYTHON"

"""

# string = "PYTHON"

# num = len(string)

# a = reversed(string)
# print(''.join(a))

# print(string[::-1])

"""
아래의 전화번호에서 하이푼을 제거하고 출력하세요. 

phone_number = "010-1111-2222"
"""
# phone_number = "010-1111-2222"
# phone_number = "010-1111-2222"
# # ## 방법 1
# print(''.join(phone_number.split('-')))

# ## 방법 2

# print(phone_number.replace("-"," "))

"""
문제의 전화번호를 아래와 같이 모두 붙여 실행하세요. 

실행 예
01011112222

"""
# phone_number = "010-1111-2222"

# print(''.join(phone_number.split('-')))

# print(phone_number.replace('-',''))

"""
url에 저장된 웹 페이지 주소에서 도메인을 출력하세요. 
"""
# url = "http://sharebook.kr"

# list_domain = url.split(".")
# print(list_domain[1])

# string = 'abcdfe2a354a32a'

# print(string.replace('a','A'))

""" 
문자열 합치기 
"""

" 화면에 '-'를 80개 출력하세요. "

# print('-'*80)

"""
문자열 출력 

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
-> % formatting를 사용해서 출력 
"""
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름 : %s 나이 : %d" % (name1, age1))
# print("이름 : %s 나이 : %d" % (name2, age2))

# """
# f 스트링 이용
# """

# print(f"이름={name1} 나이={age1}")
# print(f"이름={name2} 나이={age2}")


"""

문자열 슬라이싱 

다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"

"""

# 분기 = "2020/03(E) (IFRS연결)"

# print()

## 공백 제거

# data = " jebal degiup  "

# print(data.strip())

# print(data.replace(' ',''))

"""
upper 메서드 -> 대문자로 변경 
"""

# munja = 'asdf'

# print(munja.upper())


"""
lower 메서드 
"""

"""
capitalize 메서드

문자열의 앞에 문자만 대문자로 변경 
"""

# munja = "hello"

# print(munja.capitalize())

"""
endswith 메서드 

파일이름이 문자열로 저장되어 있을 때 endswith 메서드를 이용해서 파일 이름이 xlsx로 끝나는지 확인한다. 
"""

# file_name = "보고서.xslx"

# print(file_name.endswith('xslx','xls'))


"""
파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일이름이 '2024'로 시작되는지 확인한다. 
"""

# file_name = "2024_file.xlsx"

# print(file_name.startswith('2024'))

""" 
변수에 오른쪽 공백이 존재할 때 제거 방법 -> rstrip()
"""

# data = "039490     "

# print(data.rstrip())


##### 파이썬 문자열 041 ~ 050까지 수행


"""
파이썬 리스트 
"""

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]

# movie_rank.insert(1,'슈퍼맨')

# print(movie_rank)

# del movie_rank[2]

# movie_rank.remove("럭키")

# print(movie_rank)

"""

lang1과 lang2 리스트를 모두 가지고 있는 새로운 리스트를 만들어라. 
>> lang1 = ["C", "C++", "JAVA"]
>> lang2 = ["Python", "Go", "C#"]

"""
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]


lang3 = lang1+lang2

print(lang3)

####### 056까지 수행 