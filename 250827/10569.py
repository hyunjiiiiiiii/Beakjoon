# 다면체

T = int(input())

for i in range(T):
    V, E = map(int, input().split())

    space = 2 - V + E
    print(space)