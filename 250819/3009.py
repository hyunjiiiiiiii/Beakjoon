# 네 번째 점

X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

if X1 == X2 == X3:
    X4 = X1
elif X1 != X2 and X1 != X3:
    X4 = X1
elif X2 != X1 and X2 != X3:
    X4 = X2
else:
    X4 = X3

if Y1 == Y2 == Y3:
    Y4 = Y1
elif Y1 != Y2 and Y1 != Y3:
    Y4 = Y1
elif Y2 != Y1 and Y2 != Y3:
    Y4 = Y2
else:
    Y4 = Y3

print(X4, Y4)