import requests
from bs4 import BeautifulSoup

def get_examples():
    req = requests.get('https://google.com')
    print(f"status Code : {req.status_code}")
    print(f"Response : {BeautifulSoup(req.content,'html.parser')}")


# main 파일에서 실행될 때만 아래의 코드가 실행되고, 
# import로 실행할 때에는 실행되지 않는다. 
# if __name__ == '__main__':
#     get_examples()

get_examples()