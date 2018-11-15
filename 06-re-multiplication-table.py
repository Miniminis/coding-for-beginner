# 몇 단을 출력할 것인지 사용자로부터 받기
# 사용자 대답에 맞춰 계산 결과 보여주기

dan = int(input("몇 단을 출력하시겠습니까?"))
for num in range(1, 10):
    print("{} * {} = {}".format(dan, num, dan*num))
