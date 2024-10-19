from person import Person

class Programmer(Person):
    def __init__(self, name, age, language=None):
        super().__init__(name, age, "programmer")  # 부모 클래스의 생성자 호출
        self.language = language if language else "Python"

    def introduce(self):
        # super().hello()
        self.hello()
        print(f"나는 {self.language}언어로 개발할 수 있는 {self.name}입니다.")
