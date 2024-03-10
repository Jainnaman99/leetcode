class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result=""
        
        for i in order:
            # print(i)
            while(i in s):
                result+=i
                s=s.replace(i,'',1)
        # print(s)
        # s1=''.join(sorted(s))
        result +=s

        return result