"""

판다스에 대하여 

https://colab.research.google.com/drive/1TfjO7knC1umGr3UNqdg5ri5o2pF0ngID

"""

import pandas as pd 
import numpy as np

## 딕셔너리 

dict_data = {'이름' : '박원진', '나이' : 26}

series_data = pd.Series(dict_data)

print(type(series_data))

print(series_data)

## 리스트 

list_data = ['2024-08-11',3.14,'abc',True]

series_data = pd.Series(list_data)

print(series_data)

## 데이터 프레임 생성 

dict_data = {'c0': [1,2,3] , 'c1' : [4,5,6], 'c2':[7,8,9]}


df = pd.DataFrame(dict_data)

print(type(df))

print(df)

with open('../Readme.md',mode="r") as file:

    content = file.read()

    for line in content.splitlines():
        print(line.strip())

print(content)

