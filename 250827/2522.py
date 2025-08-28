# 별 찍기 - 12

N = int(input())

for i in range(1, N):
    block = int(2*(N-i) / 2)
    print(" " * block + "*" * i)

for i in range(N, 0, -1):
    block = int(2 * (N - i) / 2)
    print(" " * block + "*" * i)