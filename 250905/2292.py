# 벌집

N = int(input())

cnt = 1
sum = 1

if N == 1:
    print(cnt)

else:
    for i in range(1, N):
        cnt += 1
        sum += 6*i
        #print(sum)
        if N <= sum:
            break
        else:
            continue
    print(cnt)