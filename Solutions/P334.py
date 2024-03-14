class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a=max(nums)
        b=max(nums)
        for i in range(len(nums)):
            if(nums[i]<a):
                a=nums[i]
            elif(nums[i]>a and nums[i]<b):
                b=nums[i]
            elif(nums[i]>a and nums[i]>b):
                return True
        return False