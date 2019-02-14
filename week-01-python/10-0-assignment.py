# # 미니과제 1. 랜덤 뽑기
# import random
# list1 = [1, 2, 3, 4, 5]
# print(random.choice(list1))

# 미니과제 2. 클래스 만들어 보기

class School:
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

school1 = School("ewha", "1886", "Seadeamungu")
print(school1.address)
print(school1.name)
print(school1.year)
