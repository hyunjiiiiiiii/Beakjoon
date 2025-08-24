# 주사위 게임

N = int(input())
i = 0
sum = list()

while i < N:
    a, b, c = map(int, input().split())

    if a==b==c:
        sum.append(10000+a*1000)
    elif a==b and b!=c:
        sum.append(1000+a*100)
    elif b==c and c!=a:
        sum.append(1000+b*100)
    elif c==a and a!=b:
        sum.append(1000+c*100)
    else:
        sum.append(max(a, b, c)*100)

    i+=1

#print(sum)
print(max(sum))
