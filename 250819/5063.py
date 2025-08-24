# TGN

# N
# r 광고X 수익, e 광고O 수익, c 광고 비용

N = int(input())

for i in range(1, N+1):
    r, e, c = map(int, input().split())
    if (e - c) > r:
        print("advertise")
    elif (e - c) < r:
        print("do not advertise")
    else:
        print("does not matter")

