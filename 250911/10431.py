# # 줄세우기

P = int(input())

for i in range(P):
    T_list = []
    T_list = list(map(int, input().split()))

    idx = 0
    cnt = 0

    for j in T_list:

        if idx == 0 or idx == 1:
            idx += 1
            continue
        else:
            check = 1
            while check < idx:

                if T_list[idx] < T_list[check]:
                    cnt += 1
                    check += 1
                else:
                    check += 1
                    continue
        
        idx += 1
        
    print(T_list[0], cnt)




# P = int(input())

# for i in range(P):
#     T_list = []
#     T_list = list(map(int, input().split()))

#     idx = 0
#     move = 0

#     for j in T_list:

#         if idx == 0 or idx == 1:
#             idx += 1
#             continue
#         else:

#             check = 1
#             while check < idx:

#                 if T_list[idx] > T_list[check]:
#                     check += 1
#                     continue
#                 else:
#                     move += (idx-check)
#                     T_list.insert(check, T_list[idx])
#                     T_list.remove(T_list[idx])
#                     break
#             idx += 1

#     print(T_list[0], move)

    