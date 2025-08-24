# 저작권

# 멜로디의 개수 / 수록된 곡의 개수, 올림 ceil

# A: 수록된 곡, I: 평균값
A, I = map(int, input().split())

M = A * (I - 1) + 1
print(M)



