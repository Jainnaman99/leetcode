class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumval=0
        max_length=0
        d={}
        for i,num in enumerate(nums):
            sumval+=1 if num==1 else -1
            if(sumval==0):
                max_length=i+1
            elif(sumval in d):
                max_length=max(max_length,i-d[sumval])
            else:
                d[sumval]=i
        return max_length