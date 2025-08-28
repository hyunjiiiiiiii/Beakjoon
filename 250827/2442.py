# 별 찍기 - 5

N = int(input())

for i in range(1, N+1):
    block = int(2*(N-i) / 2)
    print(" " * block + "*" * (i*2-1))