class A:
    def method(self):
        print("I'm A")

class B(A):

    def method(self):
        print("I'm B")


class C(A):

    def method(self):
        print("I'm C")


## 다중 상속의 경우, MRO에 따라 super 메서드 없이도 부모클래스의 메서드를 자동으로 찾는다. 
class D(B,C):
    pass

d = D()
d.method()
print(D.mro())
