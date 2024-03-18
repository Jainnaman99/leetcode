class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i] in l:
                return False
            l.append(d[i])
        return True