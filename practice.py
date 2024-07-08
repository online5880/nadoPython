# # while
# customer = "토르"
# Index = 5
# while Index >= 1:
#     print("{}, 커피가 준비되었습니다. {} 번 남았어요".format(customer,Index))
#     Index -= 1
#     if Index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# Index = 1
# while True:
#     print("{}, 커피가 준비되었습니다.호출 {} 회".format(customer,Index))
#     Index += 1

customer = "토르"
person = "Unknown"

while person != customer:
    print("{}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")