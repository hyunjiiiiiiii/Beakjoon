# 소인수 분해

import math

N = int(input())

# 소수
sosu = list()

def is_sosu(n):
    for i in range(2, math.sqrt(N) + 1):
        if n % i == 0:
            return False
        
    return True

while N == 1:
    list

