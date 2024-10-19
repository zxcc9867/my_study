class Person:

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def hello(self):
        print(f"hello !")

    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음수일 수 없습니다.")
        else:
            self.age = age
