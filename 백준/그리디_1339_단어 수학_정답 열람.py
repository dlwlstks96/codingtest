# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
answer = 0
pocket = []

for _ in range(n):
    alphabet = input()
    pocket.append(alphabet)

for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet) - i - 1)
        alphabet_dict[alphabet[i]] += num

for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)

'''아래가 내 풀이
n = int(input())
words = []
max_str_len = 0 #단어 최대 길이
for i in range(n):
    tmp = str(input())
    words.append(tmp) #단어 저장
    max_str_len = max(max_str_len, len(tmp)) #단어 최대 길이
    
for i in range(len(words)):
    tmp = max_str_len - len(words[i])
    words[i] = ('0'*tmp) + words[i] #자릿수 맞춰주기
    
alphabet = ['A', 'B', 'C', 'D', 'E', 
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
            ]

words_dic = {}
for i in range(len(alphabet)):
    words_dic[alphabet[i]] = [] #알파벳들이 몇번째 인덱스에 나왔는지

for i in range(max_str_len):
    for j in range(len(words)):
        if words[j][i] != '0':
            words_dic[words[j][i]].append(i)
            
#print(words_dic)

count = 9 #점점 줄여가며 알파벳에 대입할 가중치
idx = 0 #몇번째 인덱스에 나온 알파벳인지 확인하기 위함
visit = [0 for i in range(len(alphabet))]
while True: 
    tmp = [] #알파벳을 비교하기 위한 리스트
    for j in range(len(alphabet)):
        if idx in words_dic[alphabet[j]] and visit[j] == 0:
            tmp.append(alphabet[j]) #알파벳 대입
    print(tmp)
    
    if len(tmp) == 1: #tmp에 혼자일때
        words_dic[alphabet[j]] = count
        count -= 1
        idx += 1
    # else: #tmp에 둘 이상일때
    #     for 
    
    
    
    count -= 1
    idx += 1
    
    if idx > 7:
        break

#print(tmp)











    
# words_val = {} #알파벳별 가중치를 담기 위함
# words_check = {} #알파벳에 가중치 넣었는지 체크하기 위함
# val_count = 9 #매번 최댓값 넣기 위한 카운트
# for i in range(max_str_len):
#     tmp = [] #같은 인덱스의 숫자들 넣어서 비교할 리스트
#     for j in range(len(words)):
#         if words[j][i] != '0' and words_check[words[j][i]] != 1: #0이 아닌 알파벳일 경우, 이미 처리한 알파벳이 아닐 경우
#             tmp.append(words[j][i])
#     print(tmp)   
#     if len(tmp) == 1 and words_check[tmp[0]] != 1: #단어 하나 들어왔을 경우
#         words_val[tmp[0]] = val_count #현재의 최댓값 대입
#         words_check[tmp[0]] = 1 #해당 단어 처리 체크
#         val_count -= 1
#     #else: #tmp에 단어가 두 개 이상일 경우
        
    
'''