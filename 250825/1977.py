# 완전제곱수
import math

M = int(input())
N = int(input())

num_list = []
m = math.ceil(math.sqrt(M))
i = m ** 2

while i <= N:
    
    num_list.append(i)
    m += 1
    i = m ** 2
    # print(i)

# print(num_list)
if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))