# 평균은 넘겠지


C = int(input())

for i in range(C):
    score_list = list(map(int, input().split()))
    #print(score_list)

    idx = 0
    total = 0
    for j in score_list:
        if idx == 0:
            N = j
            idx += 1
        else:
            idx += 1
            total += j
    avg = total / N
    #print(total, N)
    #print(avg)

    cnt = 0
    for k in score_list:
        if k > avg:
            cnt += 1
        else:
            continue
    #print(cnt, N)
    print(f"{(cnt / N) * 100:.3f}%")

