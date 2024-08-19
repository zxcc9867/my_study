import matplotlib.pyplot as plt 



"""

matplot에 대해서 

"""

# 리스트의 값들이 y값들이라고 가정하고 , x 값 [ 0, 1, 2, 3] 을 자동으로 만들어 낸다. 

# plt.plot([2,3,4,5])

# plt.show()

## 2개의 리스트 입력 

# 순서쌍 ( x,y )으로 매칭된 값을 좌표 평면 위에 그래프 시각화 

"""
( 1,1,) , (2,4 ) , ( 3, 9 ) , ( 4,16 )으로 매칭 

"""
# plt.plot([1,2,3,4], [1,4,9,16], label = 'Square')

# plt.xlabel('X-Label')

# plt.ylabel('Y-Label')

# # plt.xlim([0,15]) # x 값의 범위를 0 ~ 15로 설정 

# # plt.ylim([0,16]) # y 값의 범위를 0 ~ 15로 설정 

# # axis() 함수를 통해 x와 y의 범위를 동시에 설정 가능하다. 

# plt.axis([0,6,0,16])

# plt.legend() # 범례 적용
# plt.show()


# plt.plot([1,2,3],[5,5,5], '-', color='C0', label='Solid')
# plt.plot([1,2,3],[7,7,7], '--', color='C0', label='Dashed')
# plt.plot([1,2,3],[2,2,2], linestyle=(0,(5,3)), color='C0',label='Dotted')
# plt.plot([1,2,3],[1,1,1], linestyle=(0,(3,5,1,5)), color='C0',label='Dash-dot')

# plt.xlabel('Xlabel')
# plt.ylabel('Ylabel')
# plt.axis([0.8,3.2,1,9])
# plt.legend(loc='upper right', ncol=2)
# plt.tight_layout()

# plt.show()

"""

마커 설정 

"""


# plt.plot([4,5,6], "b")
# plt.plot([3,4,5],"ro")
# plt.plot([2,3,4], linestyle='-',marker='s', color='violet')
# plt.plot([1,2,3], linestyle='--', marker="d" , color = 'k')
# plt.plot([0,1,2], marker='$A$')

# plt.title('< Graph Title >', loc='center',pad=20) 

# plt.show()

"""

막대 그래프 생성 

"""

# x = [ 1, 2, 3] # xticks를 통해 years 리스트 안에 들어가 있는 값을 1 , 2, 3 순서대로 막대 그래프에 배치한다. 

# years = ['2022', '2023', '2024']

# values = [300, 100, 700]

# plt.bar(x,values, color=['r','g','b'], width=0.4) # x의 값에 1, 2, 3을 넣고, y의 값에 values의 값을 넣는다.  

# plt.xticks(x,years) # x 값인 1,2,3을 years 값을 차례대로 매핑한다. -> 즉, x의 1,2,3은 , 2022 , 2023 , 2024로 설정된다. 

# plt.show()

"""

산점도 

"""


# import numpy as np 

# np.random.seed(0) # 한번 랜덤한 숫자를 생성하고, 다시 실행을 누르면, 이전에 출력된 값이 출력이 된다. 즉, 해시값을 가지고 있다라고 이해하면 된다. 

# n = 100

# x = np.random.rand(n)

# y = np.random.rand(n)

# size = (np.random.rand(n) * 20) ** 2 # 동그라미 크기 

# colors = np.random.rand(n) # 색깔 

# plt.scatter(x,y , s=size, c=colors)

# plt.show()

"""

서브 플롯으로 여러개의 그래피를 그리기 

"""

import numpy as np

# linspace : 몇 등분할지 생각하면 디폴트는 50 

x1 = np.linspace(0,4) # 0부터 4까지 50 등분


x2 = np.linspace(0,4)

print(x1)

y1 = np.cos(2*np.pi * x1 ) 

y2 = np.cos(2* np.pi * x2)

plt.subplot(2,1,1) # 2개의 행 , 1개의 열로 , 그리고 첫번째 -> 2개의 그래프를 그리기 때문에 

plt.plot(x1,y1,'o-')

plt.title('1st Graph')

plt.subplot(2, 1, 2)

plt.plot(x2,y2, '.-')

plt.title('2nd Graph')

plt.tight_layout() # 모서리와 서브플롯의 모서리 사이의 여백을 설정 

plt.show()