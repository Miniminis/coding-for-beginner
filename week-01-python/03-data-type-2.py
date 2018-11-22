# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print("list")
list_a = [1,2,3]
print(list_a)
print(list_a[0])
print(list_a[1])
print(list_a[2])

#slice
print(list_a[0:3])
#applendix
list_a.append(7)
print(list_a)

list_a.remove(2)
print(list_a)

list_a.clear()
print(list_a)

# tuple (1, )
print("tuple")
tuple_a = (1,2,3)
print(tuple_a)
print(type(tuple_a))

# typle은 추가를 할 수 없다: 왜 쓸까? 프로그래머가 해당 내용을 수정하고 싶지 않게 의도함
tuple_a.append(4)

# dict (map) {}
# key & value: 키와 값으로 구별이 된다
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])

# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set set([]) 집합
set_a = set([1,2,3,3,3,3,2])
set_b = set([2,4,6])
print(set_a)
print(set_b)

# 집합 - 교집합, 합집합, 차집합, 여집합
# set은 list(단순나열)과 다르게 중복 자동 제거의 기능!!!
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
