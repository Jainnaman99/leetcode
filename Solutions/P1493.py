class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        if(0 not in nums):
            return (len(nums)-1)
        l=0
        z=0
        ans=0
        for r in range(len(nums)):
            if(nums[r]==0):
                z+=1
            while(z>1):
                if(nums[l]==0):
                    z-=1
                l+=1
            ans=max(ans,r-l)
        return ans