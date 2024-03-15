class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a,b=0,0
        if(s==''):
            return True
        while(a<len(s) and b<len(t)):
            if(s[a]==t[b]):
                a+=1
                if(a==len(s)):
                    return True
            b+=1
        return False