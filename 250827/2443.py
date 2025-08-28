# 별 찍기 - 6

N = int(input())

for i in range(N, 0, -1):
    block = int(2 * (N - i) / 2)
    print(" " * block + "*" * (2 * i - 1))