class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        listOne = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        listTwo = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        listThree = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        
        answer = []
        for word in words: #첫 글자가 어느 리스트에 포함되어 있는지 확인
            list_check = 0
            if word[0].lower() in listOne:
                list_check = 1
            elif word[0].lower() in listTwo:
                list_check = 2
            elif word[0].lower() in listThree:
                list_check = 3
                
            if list_check == 0: #첫 글자부터 어느 리스트에도 포함 X
                continue
                
            check = True
            for w in word[1:]: #나머지 단어들이 전부 같은 리스트에 포함되어 있는지 확인
                if list_check == 1 and w.lower() not in listOne:
                    check = False
                    break
                elif list_check == 2 and w.lower() not in listTwo:
                    check = False
                    break
                elif list_check == 3 and w.lower() not in listThree:
                    check = False
                    break
                    
            if check == True:
                answer.append(word)
                
        return answer
