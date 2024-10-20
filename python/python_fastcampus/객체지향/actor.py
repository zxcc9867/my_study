from person import Person

class Actor(Person):
    def __init__(self, name,age,flim):
        # 다형성 부분부터 
        super().__init__(name, age, "actor")  # 부모 클래스의 생성자 호출
        self.flim = flim
    def introduce(self):
        super().hello(self.name)
        print(f"저의 대표작은 {self.flim}입니다.")