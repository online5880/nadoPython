# 사전 (dictionary)

cabinet = {3:"유재석", 100:"김태호"}

# value 얻어오기
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# 대괄호로 가져올 때 값이 없으면 오류가 나면서 프로그램이 종료된다. 
# print(cabinet[5])
# print("hi")

# get() 으로 가져오면 "None"이 뜨면서 프로그램이 종료되지 않는다.
print(cabinet.get(5))
print("hi")

# 값이 있는지 확인
print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
# 기존에 키가 있으면 값 업데이트, 없으면 키와 값 추가
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
# 키 삭제
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
# 모든 값 제거
cabinet.clear()
print(cabinet)