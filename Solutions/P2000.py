class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l1=[]
        j=0
        for i in range(len(word)):
            if ch in word:
                if(word[i]==ch):
                    l1.append(word[i])
                    j=i+1
                    break
                else:
                    l1.append(word[i])
            else:
                return word
        l1=l1[::-1]
        s1="".join(l1)
        # print(string)
        return s1+word[j:len(word)]