class Solution:
    def compress(self, chars: List[str]) -> int:
        d={}
        n=0
        res=''
        c=chars[0]
        for i in chars:
            if(i not in d and i==c):
                d[i]=1
            elif(i in d and i==c):
                d[i]+=1
            elif(i not in d or d[i]==0) and i!=c:
                if(d[c]==1):
                    res=res+c
                    d[c]=0
                elif(d[c]>1):
                    res=res+c
                    res=res+str(d[c])
                    d[c]=0
                c=i
                d[i]=1
        if(d[chars[len(chars)-1]]==1):
            res+=chars[len(chars)-1]
        else:
            res+=chars[len(chars)-1]+str(d[chars[len(chars)-1]])
        for i in range(len(res)):
            chars[i]=res[i]
   
        return len(res)