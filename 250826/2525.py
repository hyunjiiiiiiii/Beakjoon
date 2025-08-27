# 오븐 시계

A, B = map(int, input().split())

C = int(input())

up = (B + C) // 60
min = (B + C) % 60

si = (A + up) % 24

print(si, min)
