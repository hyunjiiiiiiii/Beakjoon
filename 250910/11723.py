# 집합 - 시간초과

S = set()

M = int(input())

for i in range(M):

    ip = input()
    if ' ' in ip:
        P, X = ip.split()
    else:
        P = ip

    if P == "add":
        S.add(int(X))
        # print(S)

    elif P == "remove":
        try:
            S.remove(int(X))
        except:
            continue
        # print(S)

    elif P == "check":
        if int(X) in S:
            print(1)
        else:
            print(0)

    elif P == "toggle":
        if int(X) in S:
            try:
                S.remove(int(X))
            except:
                continue
        else:
            S.add(int(X))

    elif P == "all":
        S.update(range(1, 21))
        #print(S)

    elif P == "empty":
        S = set()
        # print(S)