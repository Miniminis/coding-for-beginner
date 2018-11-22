# # 01 o
# print("Hello World")
# # 02 o
# print("Mary's cosmetics")
# # 03 x
# print("신씨가 소리질렀다. "도둑이야".")
# # 04 x
# print("C:Windows")
# # 05 x
# print("안녕하세요.\n만나서\t\t반갑습니다.")
# # 06 o
# print("오늘은", "일요일")
# # 07 o
# print("naver;kakao;sk;samsung")
# # 08 o
# print("naver/kakao/sk/samsung")
# # 09 x
# print("first");print("second")
# # 10 x
# string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
# print(string)
#
# # Total: 5/10

# 해설
# 01
print("Hello World")
print('Hello World')

# 02
print("Mary's cosmetics")
print('Mary\'s cosmetics')

# 03
print('신씨가 소리질렀다. "도둑이야".')
print("신씨가 소리질렀다. \"도둑이야\".")

# 04
print("c:\\Windows")

# 05
# "역슬래쉬 + n"은 줄바꿈 기호로 사용합니다. 안녕하세요 이후 줄바꿈이 된 것을 확인할 수 있습니다. \t은 수평 탭을 삽입합니다.
print("안녕하세요. \n만나서\t\t반갑습니다.")

# 06
print("오늘은," , "일요일")
print("오늘은", 13, "일")

# 07
# print 함수가 제공하는 sep 이라는 기능을 사용 해보겠습니다. sep은 print 함수에서 여러 단어를 연결 할 때, 구분자로 삽입되는 문자를 정의합니다. 아래는 데이터와 데이터 사이에 공백 대신 콜론을 출력하는 코드입니다.
print("naver", "kakao", "sk", "samsung", sep=";")
# sep을 지정하지 않을 경우 그 값이 공백으로 설정되기 때문에, 006번 문제에서 단어 사이에 공백이 추가되는 것입니다. sep을 사용한 코드는 구분자의 수정 발생 시 장점이 드러납니다. 구분자가 +로 바뀌어 "naver+kakao+sk+samsung"로 변경을 하는 경우, sep 부분의 한 글자만 수정하면 됩니다.

#08
print("naver", "kakao", "sk", "samsung", sep = "/")

# 09
# 기본적으로 print 함수는 문자열 혹은 숫자를 출력하고, 그 끝에 줄바꿈문자를 삽입합니다. 끝에 삽입되는 구분자를 변경하는 기능이 end 입니다. 아래 코드는 first라는 단어를 출력하고 그 끝에 줄바꿈 문자를 두번 출력합니다.
# 문자열을 출력하고 줄바꿈 줄바꿈 대신에 한칸의 공백을 삽입하면 한줄에 두 개의 단어를 출력할 수 있습니다.
print("first", end = "\n\n")
print("first", end = ''); print("second")

# 10
# len() 함수
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))
