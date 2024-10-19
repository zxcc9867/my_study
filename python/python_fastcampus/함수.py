"""

함수

"""

# def func():
#     print("hello")

# func()

"""
기본 매개 변수는 
매개 변수 명 = 기본값 형태로 정의한다. 

def srudy(name, age=20):
"""

""


# def welcome(city, name="Guest", room=None):
#     if room is None:
#         room = []
#     room.append(101)
#     print(
#         f"Welcome, {name}! your room is {room}",
#     )


# welcome("seattle", "Python")
# welcome(name="Park", city="saitama")

"""
키워드 인자 실습 
"""

# def display(age,city,name='Guest'):
#     print(f"name : {name} , age : {age} , city : {city}")

# display("alice", 20 , "new work") # 함수의 매개 변수와 위치가 다르게 되면, 변수에 의도 하지 않은 값들이 들어가게 된다. 

# display(age=20, city="seoul", name="bob") # keyword argument