class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z=maxsize=size=0
        left=right=0
        for right in range(len(nums)):
            if(nums[right]==0):
                z+=1
            if(z>k):
                if(nums[left]==0):
                    z-=1
                left+=1
            size=right-left+1
            maxsize=max(size,maxsize)
        return maxsize