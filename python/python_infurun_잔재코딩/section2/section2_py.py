"""

find function

"""

# string = 'find function'

# print(string.find('f',3)) # 3번째 인덱스 뒤에서 부터 f가 나오는 것을 찾는다.

# print(string.find('f', 0, 5)) # 0번째부터 5번째 인덱스 사이에서 f가 나오는 것을 찾는다.


"""

example 

"""

# num = input("주민번호를 입력하세요 : ")
# if int(num.split("-")[1][1:3]) < 9:

#     print("busan")
# elif int(num.split("-")[1][0:2]) >= 9:
#     print("seoul")

"""

소인수 분해 

"""


def factor_divider(num: int) -> list:
    factors = []
    input_num = num  # num to be divided
    divder = 2
    while num > 1:

        if num % divder == 0:
            factors.append(divder)
            num //= divder
        else:
            divder += 1
            print(divder)
    return (
        f"숫자 {input_num} 에서 {factors} 로 소인수분해가 됩니다."
        if factors
        else f"{input_num} 에서 소인수분해할 수 없습니다"
    )


print(factor_divider(int(input("숫자를 입력하세요. : "))))
