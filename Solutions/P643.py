class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # maxsum=float('-inf')
        if(len(nums)==1):
            return float(nums[0])
        maxsum=currsum=sum(nums[:k])
        
        for i in range(k,len(nums)):
            currsum+=nums[i]-nums[i-k]
            maxsum=max(maxsum,currsum)
        maxsum/=k
        return maxsum