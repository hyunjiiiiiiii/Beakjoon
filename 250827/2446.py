# 별 찍기 - 9

N = int(input())

for i in range(N, 1, -1):
    block = int(2 * (N - i) / 2)
    print(" " * block + "*" * (2 * i - 1))

for i in range(1, N + 1):
    block = int(2*(N-i) / 2)
    print(" " * block + "*" * (i*2-1))

