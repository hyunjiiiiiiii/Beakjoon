# ZOAC 4_fail 250902


H, W, N, M = map(int, input().split())

row = 0
col = 0
row_cnt = 0
col_cnt = 0

while row < H:
    row_cnt += 1
    row += N + 1

while col < W:
    col_cnt += 1
    col += M + 1

print(row_cnt * col_cnt)





















# H, W, N, M = map(int, input().split())

# I = 0
# i = 0
# J = 0
# cnt = 1
# first = 0

# # 첫번째 줄
# for j in range(W):
#     #print(j)
#     if j - J > M:
#         #print(i, j)
#         I = i
#         J = j
#         cnt += 1
#     else:
#         continue
# J = 0

# while True:

#     if i - I > N:
#         income = 1
#         I = i
#         first += 1
#         # print(i, first)

#         for j in range(W):
#             #print(j)
#             if j - J > M:
#                 #print(i, j)
#                 J = j
#                 cnt += 1
#             else:
#                 continue
    
#     i += 1
#     J = 0
#     income = 0
#     #print(i)

#     if i > H:
#         break
    
        
            
# print(cnt+first)