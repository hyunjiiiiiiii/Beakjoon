# 주사위 게임

A = 100
B = 100

n = int(input())

for i in range(1, n+1):

    a, b = map(int, input().split())

    if a>b:
        B -= a
    elif a<b:
        A -= b

print(A)
print(B)