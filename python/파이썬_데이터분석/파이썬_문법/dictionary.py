"""

딕셔너리 자료형 

키 - 값으로 이루어져있다. 

"""

dict = {"key1": "key-1", "key2": "key-2", "ram": "ram"}

dict["ram"] = "ram1"


print(dict["key1"])

print(dict.keys())

print(dict.values())

## 해당 키가 딕셔너리 안에 있는지 확인하는 것

print("ram" in dict)  # 부울 형태로 출력된다.

## get() key로 값을 얻는 것

print(dict.get("key1"))

## items() : key , value 쌍 얻기

print(dict.items())

# clear() -> 키와 쌍 모두 지우기
