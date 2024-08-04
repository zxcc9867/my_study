"""

모듈에 대해서 

-> 여러 변수와 함수를 가지고 있는 집합 

< 내부 모듈 > 

내부 모듈은 파이썬에 기본적으로 내장되어 있는모듈 

ex . ) 

math , os, random , numbers , time , io 등등 

-> import 모듈 이름 

"""

import math 

# print(math.ceil(1.2)) # 올림 
# print(math.floor(1.2)) # 내림 


"""

from 

모듈 내에서 필요한 것만 골라서 가져올 때 사용 

모듈에는 많은 변수와 함수가 있기 때문에 활용하고 싶은 것만 선택하여 사용 

여러 개의 가져오고 싶은 변수 또는 함수 입력 가능 

from 모듈 이름 import 가져오고 싶은 변수 또는 함수 

from 모듈 이름 import * -> import 모듈과 동일하다. 

"""


# from math import floor,ceil


# print(floor(1.2))

# print(ceil(1.2))

"""

as 구문 

"""


# import math as m 

# print(m.ceil(1.2))

# print(m.floor(1.2))


"""

< 외부 모듈 >

파이썬에서 기본적으로 제공해주는 것이 아닌 외부 사람들이 만들어서 배포한 모듈 

numpy , pandas , matplotlib , seaborn , BeautifulSoup 

-> 외부 모듈은 pip install로 다운로드 받아야한다. 



"""

# import seaborn as sns
# import matplotlib.pyplot as plt

# titanic = sns.load_dataset('titanic')


# # print(titanic.head(5))

# # print(titanic.info(5))


# sns.swarmplot(x='class',y='age',data=titanic ,hue='sex')

# plt.show()

"""

모듈 실습 

"""

from module_test.module_1 import add,print_test


result = add(1,2,3)

print_test()


print(result)


"""

패키지.모듈 


도트를 사용하여 파이썬 모듈을 디렉터리 구조로 관리할 수 있다. 

패키지 > 모듈 -> 즉, 모듈의 상위 개념이 패키지 

"""