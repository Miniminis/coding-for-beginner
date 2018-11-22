# 21
lang = 'python'
print(lang[0] + lang[2])
# 정답

# 22
license_plate = "24 가 2210"
print(license_plate[5:9])
# 정답
# 다른 답안 1)
print(license_plate[5:])
# 다른 답안 2)
print(license_plate[-4:])

# 23
string = "홀짝홀짝홀짝"
# 오답)
print(string[0, 2, 4])
# 정답)
print(string[0::2])
# 짝수만 출력할 경우는:
print(string[1::2])

# 24
string = "PYTHON"
# 오답
print(string[5, 4, 3, 2, 1, 0])
# 정답
print(string[::-1])

# 25
phone_number = "010-1111-2222"
# 오답
print(phone_number[])
# 정답
print(phone_number[0:3], phone_number[4:8], phone_number[9:13])
phone_number.replace("-", " ")
