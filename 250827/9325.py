# 얼마?

# N: 테스트 케이스 개수, s: 자동차 가격, n: 서로 다른 옵션 개수, q p: 옵션 개수 옵션 가격

N = int(input())

for i in range(N):
    total = 0
    s = int(input())
    total =+ s

    n = int(input())
    for i in range(n):
        q, p = map(int, input().split())
        total += q * p

    print(total)
