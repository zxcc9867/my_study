"""

파일 열기 , 쓰기 


파일을 열때에는 open(파일 경로, 파일 열기 모드)

open() 함수의 첫 번째 매개변수에는 파일 경로를 입력한다. 

open() 함수의 두 번째 매개변수에는 파일 열기 모드를 지정한다. 

< 파일 열기 모드 종류 > 

1. w : 쓰기 모드 

2. a : append -> 추가 모드 , 파일의 마지막에 새로운 내용을 추가할 때 사용 

3. r : 읽기 모드 

< 파일 닫기 > 

close() 함수 사용 

-> close 함수를 사용해야 파일이 닫아진다. 

-> with 구문을 통해 자동으로 닫도록 할 수 도 있다. 


< 파일 읽기 모드 > 

readline() : 텍스트 한줄씩 읽어서 반환 

- 한줄씩 읽어 출력할 때 줄 끝에 \n 문자가 있다면 빈 줄도 같이 출력된다. 

readlines() : 파일의 모든 줄을 읽어서 각각의 줄을 리스트로 반환 

strip() : 줄바꿈 문자 제거 

"""

# myfile = open('my_study/python/파이썬_데이터분석/파이썬_문법/test.txt','w') 

# myfile.write("programming ! ")

# myfile.close() 

# myfile = open('my_study/python/파이썬_데이터분석/파이썬_문법/test.txt','a')

# myfile.write("pro")

# myfile.close() 

myfile = open('my_study/python/파이썬_데이터분석/파이썬_문법/test.txt','r')



content = myfile.readline().strip() # 한줄씩 처리를 할 때 사용 , 즉 2줄이 있으면 처음실행할 때 첫줄 , 그 다음에 실행할 때 그 다음줄이 출력된다. 

print(content)
# for i in range(0,2,):
#     print(myfile.readline())

# 파일의 모든 줄을 읽는 방법 

# content = myfile.readlines() # 모든 줄을 읽어서 리스트로 반환 

# for text in myfile.readlines(): # 모든줄을 읽어서 문자열 출력 
#     print(text)

# print(content)

myfile.close()