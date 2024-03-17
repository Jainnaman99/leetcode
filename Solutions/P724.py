class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if (len(nums)==1):
            return 0
        
        lsum=0
        rsum=sum(nums)
        for i ,ele in enumerate(nums):
            rsum-=ele
            if(lsum==rsum):
                return i
            lsum+=ele
        return -1