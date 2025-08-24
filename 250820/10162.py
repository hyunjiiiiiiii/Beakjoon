# 전자레인지

# A 5분, B 1분, C 10초
# A 300초, B 60초

T = int(input())
A = 0; B = 0; C = 0

while T != 0:
    if T >= 300:
        T -= 300
        A += 1
        #print(A)
    elif T >= 60:
        T -= 60
        B += 1
        #print(B)
    elif T >= 10:
        T -= 10
        C += 1
        #print(C)
    else:
        print(-1)
        exit()

print(A, B, C)
