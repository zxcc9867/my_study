# 추상 클래스를 임포트 

from abc import ABC,abstractmethod
class Person(ABC):

    def __init__(self, name, age, job):
        self.name = name
        self.__age = age
        self.job = job
    ## 추상 메서드 선언 
    @abstractmethod
    def introduce(self):
        pass
    def _hello(self):
        print(f"hello ! I'm {self.name} , {self.__age} years old !")

    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음수일 수 없습니다.")
        else:
            self.__age = age
