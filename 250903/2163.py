# 초콜릿 자르기

N, M = map(int, input().split())

cnt = 0

m = max(N, M)
n = min(N, M)

if N == 1 and M == 1:
    print(cnt)
    exit()


# 가로 자르기
cnt += m - 1

# 세로
n = m * (n - 1)
cnt += n

print(cnt)