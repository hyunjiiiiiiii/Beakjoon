# 과자

# K 한 개 가격, N 과자 개수, M 현재 액수

K, N, M = map(int, input().split())

result = K * N - M

if result < 0:
    print(0)
else:
    print(result)