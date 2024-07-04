# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

Index = python.index("n")
print(Index)
Index = python.index("n", Index+1)
print(Index)

print(python.find("Java"))
# print(python.index("Java"))
print("hi")

print(python.count("n"))