# View 와 Url, 내 서비스 페이지마다 우편번호를 붙여주자.

# Urls.py
urls.py 에서
from . import views
이 . 의 의미는 같은 폴더로부터
- View 를 나타내는 주소를 의미
- 2개의 Urls.py
큰 개념은 first_project: 주소를 의미
그 아래 새로운 app 이 생성될 때마다 새로운 urls가 생기는 격.

# 장고는 기본적으로 admin page를 생성 및 포함. 큰 노력없이 가능.

# first_project 에서 urls.py - blog 지우기
- r'^': Regular expession 
