# Yangjojang of The Year

# test case
T = int(input())


for i in range(T):
    S_list = list()
    L_list = list()
    
    # school num
    N = int(input())
    for j in range(N):
        S, L = input().split()
        S_list.append(S)
        L_list.append(int(L))

    max_L = max(L_list)
    idx = 0
    while idx < len(L_list):
        if L_list[idx] == max_L:
            max_idx = idx
            break
        else:
            idx += 1

    print(S_list[max_idx])