"""

예외 처리 구문 

try: 

    예외가 발생할 가능성이 있는 구문 

except:

    예외가 발생했을 때 수행되는 구문 
else:

    예외가 발생하지 않았을 때 수행되는 구문 


"""

try:
    num = int(input("숫자를 입력해주세요."))
except:
    print("예외가 발생하였습니다.")
else:
    print("입력한 숫자는 ", num, "입니다.")


try:
    print("예외가 발생할 수 있는 구문")
except:
    print("예외가 발생했을 때 실행할 코드")
finally:
    print("예외 발생 여부와 상관없이 무조건 실행할 코드")


try:
    print("예외가 발생할 수 있는 코드")
except Exception as e:
    print("예외가 발생하였습니다.", e)  # Exception은 예외의 종류를 나타내고,

    # e 부분은 에외가 발생하면, 예외 객체가 e 변수에 할당되고, 예외 메시지를 출력할 수 있다.
