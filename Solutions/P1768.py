class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        r=min(l1,l2)
        merged=''

        for i in range(r):
            merged =merged+word1[i]+word2[i]
        if(l1<l2):
            merged=merged+word2[l1:]
        elif(l2<l1):
            merged=merged+word1[l2:]
        return merged