# class

#### Article variables
title1 = "development"
author1 = "marco"
content1 = "development is easy"
veiw_count1 = 0

title2 = "couching"
author2 = "marco"
content2 = "couching is very easy"
view_count2 = 0

title3 = "business"
author3 = "marco"
content3 = "business is easy, very easy"
view_count3 = 0

#### Article class
# class Article:
#     title = "development"
#     author = "marco"
#     content = "development is easy"
#     veiw_count = 0

# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "couching"
# print(article1.title)
# print(article2.title)

##### Article class with_init_
class Article:
    author = "marco"
    veiw_count = 0

# self: 약속에 접근하겠다(Class 안에서 만든 함수)
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("developement", "deveopment is easy")
article2 = Article("couching", "counching is easy")
article3 = Article("business", "business is easy")

print(article1.view_count)


##### Article class inheritance 상속
class BrunchArticle:
