# 소인수분해

N = int(input())

idx = 2

while idx <= N:
    
    if N == 1:
        break

    if N % idx == 0:
        print(idx)
        N = int(N/idx)
        # print(N)
        continue
    else:
        idx += 1