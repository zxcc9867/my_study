from person import Person


class Farmer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, "farmer")  # 부모 클래스의 생성자 호출
        self.fruit = fruit
    def introduce(self):
        super().hello(self.name)
        print(f"""안녕하세요. 저는 {self.fruit}농장을 운영하고 있는
              {self.name}이라고 합니다.""")