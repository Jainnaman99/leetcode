class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        mc=c=0
        for i in range(k):
            if(s[i] in vowels):
                c+=1
            if(c==k):
                return k
            mc=max(c,mc)
        for i in range(k,len(s)):
            if(s[i-k] in vowels):
                c-=1
            if(s[i] in vowels):
                c+=1
            if(c==k):
                return k
            mc=max(c,mc)
        return mc