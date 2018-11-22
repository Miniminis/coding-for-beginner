# 11
a = "3"
b = "4"
print(a+b)
# 오답 7 --> 정답은 34
# 이유) 문자열 34가 출력됨.

# 12
s = "hello"
t = "python"
# 오답
# print(s)\n print("!")\n print(t)
# 정답
print(s+"!"+t)

# 13
print("Hi" * 3)
#오답: Hi*3
#정답: HiHiHi
# 설명) 문자열의 곱하기는 해당 숫자만큼 문자열을 반복해서 이어 붙입니다.

# 14
a = 1
while a < 81:
    print("-")
    a = a + 1

# 2답안) 정답
print("-" * 80)

# 15
t1 = "python"
t2 = "java"

print((t1+ " " + t2 + " ")*4)

# 16
print(10*20000)
# 정답

# 17
print(2 + 2 * 3)
#답: 8
# 정답

# 18
a = "132"
print(type(a))
#답: 문자
#<class 'str'>

# 19
num_str = "720"
print(int(num_str))
# 동일정답
num = int(num_str)
print(num)

#20
num = 100
print(str(num))
# 동일정답
str1 = str(num)
print(str1)
