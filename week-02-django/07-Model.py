# Model, 데이터베이스/SQL을 (거의) 몰라도 됩니다. (1편)
* 엑셀 파일 참조
* 엑셀과 거의 다름없는 파일을 코드의 형태로 바꾸는 과정임

class Article(models.Model):    # 자료형 구분
    title = models.CharField(max_length=30) : Charater Field 길이
    contents = models.TextField() : 글은 길어질 수 있으니까
    view_count = models.IntegerField()  : 숫자형

# SQL 명령어 - excel 시트 하나 추가하기
CREATE TABLE my app_person(
    "title" serial NOT NULL PRIMARY KEY,
    "contents" varchar(30) NOT NULL,
    "view_count" varchar(30) NOT NULL
);
