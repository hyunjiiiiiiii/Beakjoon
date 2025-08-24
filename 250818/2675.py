# 문자열 반복

T = int(input())

for i in range(1, T+1):
    R, S = input().split()
    R = int(R)

    for j in S:
        print(j * int(R), end="")
    print()
