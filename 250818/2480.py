# 주사위 세개

A, B, C = map(int, input().split())

if A==B==C:
    print(10000 + A * 1000)
elif A!=B and A!=C and B!=C:
    print(100 * max(A, B, C))
else:
    if A==B:
        print(1000 + A * 100)
    elif B==C:
        print(1000 + B * 100)
    else:
        print(1000 + C * 100)
