# ZOAC 4

H, W, N, M = map(int, input().split())

I = -2
J = -2
cnt = 1

for i in range(H):
    for j in range(W):
        if j - J < M:
            continue
        elif i - I < N:
            break
        else:
            print(i, j)
            I = i
            J = j
            cnt += 1
    if i - I < N:
        continue
            
print(cnt)