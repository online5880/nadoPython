print(2+3*4) # 14
print((2+3)*4) # 20
number = 2+3*4 # 14
print(number)

number = number + 2 # 16
print(number)

number += 2 # 18
print(number)

number *= 2 # 36
print(number)

number /= 2 # 18
print(number)

number -= 2 # 16
print(number)

number %= 5 # 1
print(number)

# 절대값
print(abs(-5)) #5

# 제곱
print(pow(4,2)) # 4*4 = 16

# 최소, 최대
print(min(5, 12)) # 5
print(max(5, 12)) # 12

# 반올림
print(round(3.14)) # 3
print(round(4.99)) # 5


from math import *
# 내림
print(floor(4.99)) # 4

# 올림
print(ceil(3.14)) # 4

# 제곱근
print(sqrt(16)) # 4
