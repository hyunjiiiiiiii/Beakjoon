# 줄세우기

P = int(input())

for i in range(P):
    T_list = []
    T_list = list(map(int, input().split()))

    idx = 0
    move = 0

    for j in T_list:

        if idx == 0 or idx == 1:
            idx += 1
            continue
        else:
            print(idx)
            check = 1
            while check < idx:
                print(check)
                if T_list[idx] > T_list[check]:
                    check += 1
                    print(check)
                    continue
                else:
                    move += (idx-check)
                    T_list.insert(check, T_list[idx])
                    T_list.remove(T_list[idx])
                    break
    print(move)

    