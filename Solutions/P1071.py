class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1=len(str1)
        l2=len(str2)
        res=''
        if(str1+str2!=str2+str1):
            return res
        for i in range(1,min(l1,l2)+1):
            if(l1%i==0 and l2%i==0):
                div=i
            # print(i)
        # print(div)
        # for i in range(div):
        #     if(str1[i]==str2[i]):
        #         res+=str1[i]
        res+=str1[0:div]
        
        return res