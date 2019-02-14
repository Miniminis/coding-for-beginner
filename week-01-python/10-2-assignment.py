# 과제 2- 회사 조직도 만들기
# 구현내용: 1) 사람 클래스 하나 만들기. 기본요소는 이름, 나이 성별.
# 구현내용: 2) 직장동료 클래스를 사람 클래스를 이용해서 만듭시다. 추가사항은 직급.
## 힌트: 1) 클래스와 상속 이용하기, 2) 사람의 기본요소 이름, 나이, 성별은 각각 새로운
 # 사람을 만들 때, 입력을 받을 수 있도록 합시다.
## 힌트 3) 직장동료의 기본 직급은 대리로 지정
## 힌트 4) 사람 클래스에서 새로운 사람을 만들 떄, 입력은 그래도 유지하면서 직급도 처음
 # 만들어질 때 입력하도록 변경을 도전.

#1. 사람 클래스 만들기
# 이름, 나이, 성별
#1-1. 새로 만들때 입력
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

Human1 = Human("김철수", "40", "남")
Human2 = Human("박영이", "50", "여")
Human3 = Human("이승승", "25", "여")

#2. 직장동료 클래스 만들기
# 상속 이용하기
# #2-1. 기본 직급 = 대리
# class Colleague(Human):
#     position = "대리"
#
# Colleague1 = Colleague("이상민", "35", "여")
# print(Colleague1.name)
# print(Colleague1.age)
# print(Colleague1.gender)
# print(Colleague1.position)

# # 빠트린 내용 - 만약에 전체 정보 출력하고 싶다면?
# print(Colleague1.__dict__)

#2-2. 새로 만들때마라 입력값을 받고 싶다면?
class Colleague(Human):
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

Colleague1 = Colleague("이장고", "30", "남", "팀장")
print(Colleague1.__dict__)
