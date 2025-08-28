# 할로윈의 사탕

N = int(input())

for i in range(N):
    c, v = map(int, input().split())

    you = c // v
    dad = c % v

    print(f"You get {you} piece(s) and your dad gets {dad} piece(s).")
