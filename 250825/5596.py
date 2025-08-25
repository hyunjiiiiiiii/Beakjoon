# 시험 점수

A, B, C, D = map(int, input().split())

E, F, G, H = map(int, input().split())

S = sum((A, B, C, D))
T = sum((E, F, G, H))

if S > T:
    print(S)
elif S < T:
    print(T)
else:
    print(S)