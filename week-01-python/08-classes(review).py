# Class

title1 = "아프리카"
author1 = "minhee"
content1 = "아프리카는 재미있어요"
view_count1 = 0

title2 = "프로그래밍"
author2 = "minhee"
content2 = "프로그래밍은 재미있어요"
view_count2 = 0

title3 = "글쓰기"
author3 = "minhee"
content3 = "글쓰기는 재미있어요"
view_count3 = 0

class Article:
    author = "minhee"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("아프리카", "아프리카는 재미있어요")
article2 = Article("프로그래밍", "프로그래밍은 재미있어요")
article3 = Article("글쓰기", "글쓰기는 재미있어요")

print(article2.content)
article3.read()
article3.read()
article3.read()
article3.read()
article3.read()
print(article3.view_count)

# 상속
class FacebookArticle(Article):
    source = "페이스북"

    def read(self):
        self.view_count = self.view_count + 5

Facebook_article1 = FacebookArticle("아프리카", "아프리카는 재미있어요")
Facebook_article1.read()
Facebook_article1.read()
print(Facebook_article1.view_count)
Facebook_article3 = FacebookArticle("글쓰기", "글쓰기는 재미있어요")
print(Facebook_article3.source)
print(Facebook_article3.view_count)
