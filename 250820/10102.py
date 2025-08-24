# 개표

V = int(input())
vote = input()

if len(vote) != V:
    raise

A_cnt = 0
B_cnt = 0

for j in vote:
    if j == "A":
        A_cnt += 1
        #print(A_cnt)
    else:
        B_cnt += 1
        #print(B_cnt)

if A_cnt > B_cnt:
    print("A")
elif A_cnt < B_cnt:
    print("B")
else:
    print("Tie")