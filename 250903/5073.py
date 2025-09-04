# 삼각형과 세 변


while True:
    A, B, C = map(int, input().split())

    if A == B == C == 0:
        break

    if max(A, B, C) >= (A+B+C - max(A, B, C)):
        print("Invalid")
    elif A == B == C:
        print("Equilateral")
    elif A != B and B != C and C != A:
        print("Scalene")
    else:
        print("Isosceles")