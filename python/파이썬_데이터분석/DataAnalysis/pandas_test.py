"""

타이타닉 데이터를 가지고 판다스 실습 

"""

import pandas as pd
import numpy as np
import os


# 현재 스크립트 파일이 있는 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

file_path = os.path.join(current_dir, 'titanic.csv')

data=pd.read_csv(file_path)

# data.info()

# print(data.dtypes)

# print(data.shape)


# print(type(data))

# names = data['Name']

# print(names.head())

# print(type(names))

# passenger = data['Name']


# print(passenger.head())

# passenger = data[['Name']]

# print(passenger.head())

# print(type(passenger))

"""

판다스 데이터 필터링 

"""

# 나이가 35살 이상인 데이터를 추출 

# data_Sex=data['Sex']

# print(data_Sex.head())

# data_age = data[(data['Age'] > 35) & (data['Sex'] == 'male')]

# print(data_age.head())


### 불리언 인덱싱 

"""

.inin() # 각각의 요소가 데이터프레임 또는 시리즈에 존재하는지 파악하여 

True , False로 나타낸다. 

# 불리언 인덱싱 + .isin() -> 데이터의 특정 범위만 추출 

"""

# print(data.head(2))

# isin_test = data[data['Pclass'].isin([1])] # 해당 열에서 값이 1인 요소들에 대해 True , False 



# print(f"< Pclass가 1인 데이터만 출력> \n{isin_test.head()}")


# age2040 = data[data["Age"].isin(np.arange(20,41))]

# print(age2040.head(10))

"""

.isna , .notna

"""

# print(data['Age'].isna()[0:8]) # 0 ~ 7번째까지 결측치가 있는 것은 True

# # NoNa_data = data[data['Age'].isna() != True ].head()

# NoNa_data = data[data['Age'].notna() ].head()

# print(NoNa_data)

"""

결측지 제거 

"""

# print(data.head())

# print(data.dropna().head())

# print(data.dropna(axis=1).head()) # 결측치가 들어가 있는 열 삭제 
"""

판다스 이름과 인덱스로 특정 행과 열 선택 

"""

# data.info()

# name35 = data.loc[data["Age"] > 35 , ["Name","Age"]]

# # print(name35.head())

# # name35 = pd.DataFrame()

# # 1번째 행부터 3번째 행까지의 0번째 열의 값을 No name으로 변경 
# name35.iloc[[1,2,3],0] = "No name"

# print(name35.head())

"""

판다스 데이터 통계 

"""
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 데이터의 중앙값과 평균값을 계산
# mean_age = data["Age"].mean()
# median_age = data["Age"].median()

# # 히스토그램을 그리기 위해 seaborn의 histplot 사용
# plt.figure(figsize=(10, 6))
# sns.histplot(data["Age"].dropna(), bins=30, kde=False, color='blue')

# # 평균값과 중앙값을 그래프에 선으로 표시
# plt.axvline(mean_age, color='red', linestyle='--', label=f'Mean: {mean_age:.2f}')
# plt.axvline(median_age, color='green', linestyle='-', label=f'Median: {median_age:.2f}')

# # 그래프 제목과 레이블 추가
# plt.title("Distribution of Age with Mean and Median")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.legend()

# # 그래프 출력
# plt.show()


# print(data[["Age","Fare"]].describe())


# print(data.agg({"Age" : ["min" , "max" , "median"],
#                "Fare" : ["max" , "min"]}))


# Group By 함수로 성별과 클래스로 묶어주고 나이와 요금의 평균 구하기 

# group_by = data.groupby(["Sex","Pclass"])[["Age","Fare"]].mean()

# print(group_by)

# data.info()

# survive = data.groupby(["Sex","Pclass"])["Survived"].mean()

# print((survive*100).head())


# # .value_counts() 함수를 이용하여 개수를 구하기 

# pclass_data = data["Pclass"].value_counts()

# print(pclass_data)

# # 판다스 빈 데이터 프레임 정의 

# df = pd.DataFrame()





# df = df.append({'Name' : ['A스타' '온제드'],"Age" : [25, 26]})

# print(df)

"""

데이터 행 추가 

"""


new_data = data.iloc[0,:] # 행 번호, 열 번호 -> 첫번째 행의 모든 데이터를 들고온다. 

data.loc[891] = new_data

print(data.shape)

"""

데이터 열 추가 

"""

data.info()

data['relationship of Survive of Sex'] = data.groupby(['Sex'])['Survived'].transform('mean')

print(data.shape)
print(data.head())

"""

데이터 행 삭제 

"""

# data = data.drop(np.arange(880,890),axis=0)

"""

데이터 열 삭제 

"""

# data = data.drop('relationship of Survive of Sex', axis=1)

# print(data)
# print(data.shape)