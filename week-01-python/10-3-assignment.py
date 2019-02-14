# 과제 3 - 가위바위보 게임
# 구현 내용
# 1 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# 2 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# 3 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
# 힌트
# 1 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# 2 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# 3 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.

# 원래답안
# user = input("우리 가위바위보하자! 가위, 바위, 보!")
#
# import random
# list_rsp = ["가위", "바위", "보"]
# computer = print(random.choice(list_rsp))
#
# if user and computer = "가위" or "바위" or "보":
#     print("무승부입니다")
# elif user = "가위" and computer = "보", user = "바위" and computer = "가위", user = "보" and computer = "바위":
#     print("user님이 승리하셨습니다")
# else user = "보" and computer = "가위", user = "가위" and computer = "바위", user = "바위" and computer = "보":
#     print("computer님이 승리하셨습니다")

# 구글링 답안
# import random
# for i in range(5):
#     num = int(input("0.가위 1.바위 2.보 중 하나를 선택하세요>>\n"))
#     com = random.randrange(1,3)
#     print(com)
#
#     if num >2:
#         print("잘못누르셨습니다")
#     elif num == com:
#         print("비겼습니다")
#     elif num+1 == com or (num == 2 and com ==0):
#         print("컴퓨터님이 승리하셨습니다")
#     else:
#         print("사용자님이 승리하셨습니다")

# 마르코님 답안 * 변수입력은 오타로 인한 에러를 사전방지해주는 기능!
# random함수는 보통 맨 위에 씀

import random

rock = "바위"
scissor = "가위"
paper = "보"
rps_list = (
    rock,
    paper,
    scissor
)

win_count = 0
lose_count = 0

while win_count <3 and lose_count <3:
#1. 사용자 입력받기
    user_choice = input("우리 가위 바위 보 하자! 가위, 바위, 보!>>\n")
#2. 컴퓨터 임의 선택
    computer_choice = random.choice(rps_list)
#3. 3번 지거나 3번 이기면 게임 끝
    if  user_choice == computer_choice:
        print("비기셨습니다")
    elif ((user_choice == rock and computer_choice == scissor)
        or (user_choice == scissor and computer_choice == paper)
        or (user_choice == paper and computer_choice == rock)):
        win_count = win_count + 1
        print("이기셨습니다")
    else:
        lose_count = lose_count + 1
        print("지셨습니다")

if win_count == 3:
    print("사용자가 최종 승리하셨습니다")
else:
    print("컴퓨터가 최종 승리하셨습니다")
