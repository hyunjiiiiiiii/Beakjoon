# 0 = not cute / 1 = cute

N = int(input())

not_cnt = 0
cute_cnt = 0

for i in range(1, N+1):
    ans = int(input())
    if ans == 0:
        not_cnt += 1
    else:
        cute_cnt += 1

# print(not_cnt, cute_cnt)

if not_cnt > cute_cnt:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")