# 평균은 넘겠지_fail


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
            total += j
            idx += 1
    avg = total / N
    #print(total, N)
    #print(avg)

    cnt = 0
    for k in range(1, len(score_list)):
        if score_list[k] > avg:
            cnt += 1
        else:
            continue
    #print(cnt, N)
    result = round((cnt / N) * 100, 3)
    #print(result)
    print(f"{result:.3f}%")

