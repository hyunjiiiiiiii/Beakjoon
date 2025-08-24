# OX 퀴즈

T = int(input())


for i in range(1, T+1):
    inx = 0
    score = 0
    cnt = 0
    
    case = input()

    while inx < len(case):
        if case[inx] == "O":
            score  = score + cnt + 1
            cnt += 1
            inx += 1
        else:
            cnt = 0
            inx += 1
    print(score)