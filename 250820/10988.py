# 팬린드롬인지 확인하기

import math

word = input()

i = 1
if len(word) % 2 == 0:

    while i <= (len(word) / 2):
        if word[i-1] != word[-i]:
            print(0)
            exit()
        else:
            i += 1
            continue
    print(1)

else:
    while i <= math.floor(len(word) / 2):
        if word[i-1] != word[-i]:
            print(0)
            exit()
        else:
            i += 1
            continue
    print(1)

