# 단어 공부

word = list(input().upper())

set_word = set(word)
#print(set_word)

dict_word = {}
for i in set_word:
    dict_word[i] = 0

for j in word:
    for k in dict_word:
        if j == k:
            dict_word[k] += 1

max_cnt = 0
for v in dict_word.values():
    if v == max(dict_word.values()):
        max_cnt += 1

if max_cnt > 1:
    print("?")
else:
    max_key = max(dict_word, key=dict_word.get)
    print(max_key)



