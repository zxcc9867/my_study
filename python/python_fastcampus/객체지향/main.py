from programmer import Programmer
from actor import Actor
from farmer import Farmer

# dave = Programmer("dave", 42)
# kave = Actor("kave", 42, "기생충")
# kim = Farmer("kim", 42, "사과")

# dave.introduce()
# kave.introduce()
# kim.introduce()

## 디형성 실습

# people = [
#     Programmer("dave", 42),
#     Actor("kave", 42, "기생충"),
#     Farmer("kim", 42, "사과"),
# ]

# for person in people:
#     person.introduce()

## 캡슐화 실습

dave = Programmer("dave", 42)
dave.age = -1 # 이런식으로 인스턴스의 속성 값을 설정할 수 있다. ( 캡슐화를 하지 않으면 )\
dave._hello()