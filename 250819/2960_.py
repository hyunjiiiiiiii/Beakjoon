# 에라토스테네스의 체

N, K = map(int, input().split())
# 7, 3

P = list(range(2, N + 1))
cnt = 1
i = 0
target = 0

while i < len(P):
    if K == 1:
        print(2)
        exit()
    
    for j in range(2, N+1):

        if target <= P[-1]:
            target = P[i] * j
            #print(target)
        
            if target in P:
                P.remove(target)
                cnt += 1
                #print(cnt)

                if cnt == K:
                    print(target)
                    exit()
                else:
                    continue
        else:
            target = 0
            break

    i += 1
    cnt += 1
    target = P[i]
    #print(target)
    #print(cnt)
    if cnt == K:
        print(target)
        exit()



