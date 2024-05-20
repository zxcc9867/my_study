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
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]


# lang3 = lang1+lang2

# print(lang3)

####### 056까지 수행


"""
다음 리스트에서 최댓값과 최솟값을 출력하라. 

nums = [1, 2, 3, 4, 5, 6, 7]


"""

# nums = [1, 2, 3, 4, 5, 6, 7]

# print(f"최댓값은 {max(nums)} 최솟값은 {min(nums)}")

# min=100
# max=0
# for i in nums:
#     if i > max:
#         max=i
#     if i < min:
#         min=i
# print(f"최댓값은 {max} 최솟값은 {min}")

"""
다음 리스트의 합을 출력하라. 
"""

# nums = [1, 2, 3, 4, 5]
# num_sum = 0
# print(sum(nums))

# for i in nums:
#     num_sum = num_sum+ i

# print(num_sum)


"""
다음 리스트에 저장된 데이터의 개수를 화면에 구하라. 
"""


cook = [
    "피자",
    "김밥",
    "만두",
    "양념치킨",
    "족발",
    "피자",
    "김치만두",
    "쫄면",
    "소시지",
    "라면",
    "팥빙수",
    "김치전",
]


# print(f"리스트의 갯수는 {len(cook)}입니다.")

# print([x+'맛있겠다' for x in cook])

"""

다음 리스트의 평균을 구하라. 

"""

# nums = [1, 2, 3, 4, 5]

# print(f"리스트의 평균은{sum(nums)/len(nums)}")

"""
price 변수에는 날짜와 종가 정보가 저장되어 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. 
"""

# price = ["20180728", 100, 130, 140, 150, 160, 170]

# for i in price:
#     if type(i)==str: # 타입 자체로 비교를 해야하기 때문에, 'str'이 아닌 str이 맞다.
#         price.remove(i)

# print(f"가격 정보{price}")


# res = [x for x in range(10)] # 리스트로 만들어준다.

# print(res)

"""
슬라이싱을 사용해서 홀수만 출력하라. 
"""

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(nums[::2])

# print([x for x in nums if x%2 == 1])


"""
슬라이싱을 사용해서 역방향으로 출력하라. 
"""

# nums = [1,2,3,4,5]

# rev = reversed(nums)

# print(list(rev))

# print(nums[::-1])

"""

67. join 메서드

"""

# interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]

# print('/'.join(interest))

"""

split 메서드 

"""

# string = "삼성전자/LG전자/Naver"

# arr = string.split('/')

# print(arr)

"""
오름차순 정렬
"""

# data = [2, 4, 3, 1, 5, 10, 9]


# print(list(sorted(data)))

"""
튜플 
"""

# movie = ('닥터스트레인지','스플릿','럭키')

# 나의튜플 = (1,) # 이렇게 해야 된다.
# nums=[]
# for i in  range(2,100,2):

#     nums.append(i) # 튜플은 생성된 시점에서 불변의 존재가 되기 때문에, 먼저 리스트를 만들고, 리스트를 튜플로 만드는 것이 효율적이다.

# print(tuple(nums))

"""

별표현식


>> a, b, *c = (0, 1, 2, 3, 4, 5)
>> a
0
>> b
1
>> c
[2, 3, 4, 5]

"""

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]


# *valid_score, scores, score2 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# print(valid_score,scores,score2)


"""
딕셔너리 구성 
"""

# ice = {'메로나' : 1000,'폴라포' : 1200 , '빵빠레' : 1800}

# ice['죠스바'] = 1200
# ice['월드콘'] = 1500

# # print(ice["메로나"])

# ice["메로나"] = 1300

# # print(ice)

# ice.pop('메로나')
# print(ice)

"""
인벤토리에서 메로나의 가격을 화면에 출력하라.
"""

# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}


# # print(f"메로나의 가격은 {inventory['메로나'][0]}원 메로나의 재고는 {inventory['메로나'][1]}개")

# inventory['월드콘'] = [500,7]

# # print(inventory)

# # 딕셔너리의 키값으로 된 것만 출력

# print(inventory.keys())

# price = inventory.values()
# print(inventory.values())

# # 금액의 총합

# print(f"가격의 총합은 {sum([x[0] for x in price  ])}")

"""
update 메서드
"""

# icecream = {
#     "탱크보이": 1200,
#     "폴라포": 1200,
#     "빵빠레": 1800,
#     "월드콘": 1500,
#     "메로나": 1000,
# }
# new_product = {"팥빙수": 2700, "아맛나": 1000}

# a = icecream.update(new_product) # 이렇게 하면 출력이 안된다. update는 내부적으로 딕셔너리를 갱신하지만, 어떠한 값도 반환하지 않기 때문에 None이 출력된다.

# icecream.update(new_product)

# print(a) # None 출력

# print(icecream) # 제대로 출력

"""
zip과 dict

아래 두개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다. 
"""

# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)


# result = dict(zip(keys,vals)) # zip은 여러개의 객체를 인수로 받아서 튜플로 묶어준다.

# print(result)

"""
"""

# date = ["09/05", "09/06", "09/07", "09/08", "09/09"]
# close_price = [10500, 10300, 10100, 10800, 11000]

# print(dict(zip(date,close_price))) # zip은 여러개의 리스트도 묶을 수 있고, 이를 dict로 하면 딕셔너리가 생성된다.

## 5/8일 까지 했다.

"""
다음은 101번부터 
"""

# 파이썬 분기문

## 5/13일

"""
사용자로부터 하나의 숫자를 입력받고, 입력받은 숫자에 10을더해 출력해라. 
"""

# num = int(input("숫자를 입력하세요. : "))

# print(f"입력받은 숫자에 10을 더한 값은 {num+10}입니다.")

"""
사용자로부터 받은 단어가 리스트에 있는지 확인 
"""

# fruit = ["사과", "포도", "홍시"]

# name = input("과일을 입력하세요. ")

# if name in fruit:
#     print(f"{name}이 존재합니다.")
# else:
#     print(f"{name}이 존재하지 않습니다.")

"""
딕셔너리에서 값을 찾기 
"""

# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# name = input("과일을 입력하세요.")

# for i in fruit:
#     if fruit[i] == name:
#         print(f"{name}이 존재합니다.")
#         break
# else: # else 절은 if가 아닌 for 루프에 속한다. 즉, for 루프를 다돌고 , break로 인해 중단되지 않았을 때 실행이 된다.
#     print(f"{name}이 존재하지 않습니다.")


"""
사용자로부터 문자 한개를 입력받고, 소문자일 경우 대문자로, 대문자일 경우 소문자로 변경해서 출력해라. 
"""

# alpha = input("영문자를 입력해주세요.")

# print(alpha.upper() if alpha.islower() == True else alpha.lower() ) # 삼항 연산자 사용

"""
삼항 연산자 -> 조건이 참일 때 출력 if 조건 else 조건이 거짓일 때의 출력 
"""

"""
5/13 121까지 수행 
"""

"""

124. 사용자로부터 세 개의 숫자를 입력 받은 후, 가장 큰 숫자를 출력하라. 

map 함수 

map(function, iterable)


"""


# nums = list(map(str,input("숫자를 입력해주세요.").split()))

# print(f"가장 숫자가 높은 숫자는{max(nums)}이고, 가장 낮은 숫자는{min(nums)}입니다.")


"""
주민등록번호를 보고, 남자 / 여자인지 출력 
"""

# first , second = str(input("주민번호를 입력해주세요. ( 하이푼 포함 )")).split('-')

# [ print("남자입니다.") if int(second[0]) in [1,3] else print("여자입니다.")]

# if int(second[1]) in range(0,9):
#     print("서울")
# elif int(second[1]) in range(9,13):
#     print("부산")


"""
주민 번호 유효성 검사 

주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 
먼저 앞에서 부터 12자리의 숫자에 2,3,4,5,6,7,8,9,2,3,4,5를 차례로 곱한 뒤 그 값을 전부 더하고, 
연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록 번호의 마지막 값이 된다. 
"""
nums = input("주민번호를 입력하세요. 12자리 (하이픈 포함) : ")

# 하이픈을 기준으로 주민번호를 분리
first_number, second_number = nums.split("-")

# 하이픈을 제거하고 주민번호를 합침
full_number = list(first_number + second_number)

print(full_number)

multiple_num = [2,3,4,5,6,7,8,9,2,3,4,5]

# 결과를 저장할 리스트 초기화
numbers = []

# full_number의 각 자릿수를 순회
for i in range(0,len(full_number)):
    # 각 자릿수를 정수로 변환
    numbers.append(int(full_number[i])*multiple_num[i])

last_num = 11 - sum(numbers)%11

identity_number=nums+str(last_num)


print(identity_number)
