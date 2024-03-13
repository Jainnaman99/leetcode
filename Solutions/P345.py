class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        l1=[]
        res=''
        for i in s:
            if i in vowels:
                l1.append(i)
        l1.reverse()
        # print(l2)
        j=0
        for i in range(len(s)):
            if(s[i] in vowels):
                res=res+l1[j]
                j+=1
            else:
                res=res+s[i]
        return res