# Quiz ) 당신은 Cocoa 서비스를 이용하는 택시 기사이빈다.
# 50 명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

import random

person = 0
for i in range(1, 51):
    time = random.randint(5, 50)
    if 5 <= time <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(i,time))
        person+=1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(i,time))
        
print("총 탑승 승객 : {} 분".format(person))
        