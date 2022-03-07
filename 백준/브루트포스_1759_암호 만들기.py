# -*- coding: utf-8 -*-

import itertools as it

l, c = map(int, input().split())

data = list(map(str, input().split()))

mo = ['a', 'e', 'i', 'o', 'u']
ja = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
      'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# if 'a' > '':
#     print('sadf')

data.sort() #정렬 후 combi를 쓰기에 자연스레 알파벳 순으로만 뽑는다


res = it.combinations(data, l)
for i in res:
    i = list(i)
    mo_count = 0
    ja_count = 0
    prev = ''
    check = True
    for j in i:    
        if j in mo:
            mo_count += 1
        elif j in ja:
            ja_count += 1
        prev = j
    
    if mo_count < 1 or ja_count < 2:
        continue
    else:
        print(''.join(i))