class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d={}
        count=0
        sum=0
        for i in nums:
            sum+=i
            if(sum==goal):
                count+=1
            if(sum-goal in d):
                count+=d[sum-goal]
            if(sum in d):
                d[sum]+=1
            else:
                d[sum]=1
        print(d)
        return count            