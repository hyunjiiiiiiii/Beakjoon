# 최소공배수

T = int(input())

# for i in range(T):
#     A_in, B_in = map(int, input().split())

#     idx_A = 2
#     idx_B = 2
#     A = A_in
#     B = B_in

#     while A != B:
#         if A == B:
#             break
#         elif A < B:
#             if B % A == 0:
#                 idx_A = B // A
#                 A *= idx_A
#                 break
#             else:
#                 A = A_in
#                 A *= idx_A
#                 idx_A += 1
#                 # print(A)
#                 continue
#         else:
#             if A % B == 0:
#                 idx_B = A // B
#                 B *= idx_B
#                 break
#             else:
#                 B = B_in
#                 B *= idx_B
#                 idx_B += 1
#                 # print(B)
#                 continue
    
#     print(A)

# 유클리드 호제법
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(T):
    A, B = map(int, input().split())

    lcm = A * B / gcd(A, B)

    print(int(lcm))
