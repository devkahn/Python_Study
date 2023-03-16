# 컴퓨터의 외부 및 내부 IP 확인하기
import socket


## 내 아이피 주소
print('내 아이피 주소')
in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)


## 컴퓨터의 외부 및 내부 IP 확인
print('컴퓨터의 외부 및 내부 IP 확인')
in_addr2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr2.connect(("www.google.co.kr", 443))
print(in_addr2.getsockname()[0])


### 컴퓨터 외부 IP  알아보는 코드 만들고 실행

#pip install requests
import requests
import re

print('컴퓨터 외부 IP  알아보는 코드 만들고 실행')
req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)


#### 내부, 외부 IP 한 번에 출력하는 코드 만들고 실행

in_addr3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr3.connect(("www.google.co.kr", 443))
print("내부 IP : ", in_addr3.getsockname()[0])

req2 = requests.get("http://ipconfig.kr")
out_addr2 = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print('외부 IP : ', out_addr2)