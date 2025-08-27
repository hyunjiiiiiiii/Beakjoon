# 인공지능 시계

A, B, C = map(int, input().split())
D = int(input())

hour = D // 3600
D -= 3600*hour
min = D // 60
D -= 60*min
sec = D

e_h = A+hour
e_m = B+min
e_s = C+sec
#print(e_h, e_m, e_s)

if e_s >= 60:
    e_m += (e_s // 60)
    e_s %= 60
if e_m >= 60:
    e_h += (e_m // 60)
    e_m %= 60

e_h %= 24
print(e_h, e_m, e_s)

