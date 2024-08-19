"""
class에 대해서 

"""


class 클래스:
    pass


# 클래스로 만들어진 인스턴스가 객체가 된다.
# 인스턴스는 객체와 클래스의 관계를 말할 때 인스턴스라고 한다.
객체 = 클래스()

"""
메소드 

클래스안에 있는 함수를 의미한다. 

클래스 안에 메소드를 정의할 때 매개변수의 첫번째에는 반드시 self를 입력한다. 

< 구조 >

class 클래스 이름 : 
    def 메소드 이름 (self, 추가적인 매개변수):
        pass

"""


# class class_test:
#     def class_method(self,name:str ,age:int):
#         self.name = name
#         self.age = age

#     def class_print(self):
#         print(f"당신의 이름은 {self.name} , 당신의 나이는 {self.age}")


# isinstance_test = class_test()

# isinstance_test.class_method('박원진',26)

# isinstance_test.class_print()\


"""

< 생성자 > 

클래스로부터 인스턴스가 생성될 때 자동으로 실행되는 함수 

클래스를실행하면 가장 먼저 생성자인 '__init__ 함수가 호출 

__init__ 함수는 인스턴스의 생성과 동시에 필요한 정보를 입력 받도록 구현하는 역할 

클래스 내부의 함수의 첫번째 매개변수는 반드시 self 입력 

객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용 

"""


# class Teddy:
#     def __init__(self,color,taste) :
#         self.color = color
#         self.taste = taste
#         print(self.color, self.taste)

# jelly = [Teddy('파랑', '소다'),
#          Teddy('빨강', '딸기')]


"""

< 상속 > 

* 물려받다라는 뜻 

* 기존에 있던 클래스의 기능을 물려 받을 수 있다. 


< 상속을 하는 이유 > 

* 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경할 때 사용 

* 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황에 사용 




"""


# class parent:

#     def __init__(self, name,color) -> None:
#         self.name = name
#         self.color = color

#     def print_info(self):
#         print("부모 클래스입니다. ")
#         print(self.name,self.color)

# # 일반적으로 부모 클래스와 자식 클래스의 메소드의 이름이 같으면, 자식 클래스의 메소드가 실행된다.


# class child(parent): # parent라는 부모 클래스를 상속받았기 때문에 부모 클래스가 들고 있던 __init__이 들어가 있다.
#     # 때문에 따로 정의를 해주지 않아도 된다.
#     def print_info(self):
#         print("자식 클래스 입니다.")
#         print(self.name,self.color)
#     def print_info_all(self):
#         print('부모 클래스, 자식 클래스 모두 출력')
#         super().print_info()
#         self.print_info()

# # test1 = parent('곰돌이 젤리', '파랑')

# test1 = child('곰돌이 젤리' , '빨강')

# test1.print_info_all()


"""

< 다중 상속 >

자식 클래스를 선언할 때 소괄호로 원하는 부모 클래스를 모두 포함 

다중 상속의 개수 제한 없음 

class 부모 클래스 1 :
    pass 
    
class 부모 클래스2 : 

    pass 
    
class 자식 클래스 3 ( 부모 클래스 1, 부모 클래스2 ) :
    pass


"""
