# 댓글 이벤트
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 suffle 과 sample 을 활용

# 출력 예제
# -- 당첨자 발표--
# 치킨 당첨자 : 1
# 커피 담청자 : [2, 3, 4]
# -- 축하합니다 --

from random import *
students = list(range(1,21))

shuffle(students)

print('-- 당첨자 발표 --')
winners = sample(students,4)
print('치킨 당첨자 : {}'.format(winners[0]))
print('커피 당첨자 : {}'.format(winners[1:]))
print('-- 축하합니다 --')