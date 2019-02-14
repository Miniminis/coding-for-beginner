# 과제 1 - 맛집 고르기
# 구현내용: 1) 한식, 중식, 일식 중 한가지 고르기
# 2) 사용자 입력 받기
# 3) 대답에 맞는 식당이름을 하나 임의로 추천해주기
## 리스트 여러개 사용
## 사용자의 입력 받기

# # 원래 답안
# list_menu = ["한식", "중식", "일식"]
# list_한식 = ["딸기골", "삼진식당", "기사식당"]
# list_중식 = ["상하이", "북경반점", "사천짜장"]
# list_일식 = ["후쿠스시", "스시혼", "후루사또"]
#
# menu = input("무엇을 드시고 싶으십니까? 한식, 중식, 일식 중 한 가지를 골라서 대답해주세요")
# print("아하," + menu + "을/를 드시고 싶으시군요. 메뉴에 딱 맞는 식당을 추천해드릴게요" )
#
# import random
#
# if menu = "한식":
#     print(random.choice(list_한식))
# elif menu = "중식":
#     print(random.choice(list_중식))
# else menu = "일식":
#     print(random.choice(list_일식))

# 수정답안 1
#1 식당 리스트 만들기
list_menu = ["한식", "중식", "일식"]
list_한식 = ["딸기골", "삼진식당", "기사식당"]
list_중식 = ["상하이", "북경반점", "사천짜장"]
list_일식 = ["후쿠스시", "스시혼", "후루사또"]

#2 사용자 입력 받기
menu = input(
    "무엇을 드시고 싶으십니까? 한식, 중식, 일식 중 한 가지를 골라서 대답해주세요>>\n"
    )

#3 대답에 맞는 식당 추천하기
import random

if menu == "한식":
    menu_result = random.choice(list_한식)
    # menu_result = list_한식(random.randint(0, len(list_한식)))
elif menu == "중식":
    menu_result = random.choice(list_중식)
elif menu == "일식":
    menu_result = random.choice(list_일식)
else:
    print("한식,일식, 중식 중에서만 골라주세요")

if menu_result:
    print("원하시는 {}를 맛볼 수 있는 {}이/가 추천되었습니다".format(menu, menu_result))
