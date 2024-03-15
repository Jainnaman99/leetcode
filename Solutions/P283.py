class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1,-1,-1):
        #     if(nums[i]==0 and i!=len(nums)-1):
        #         while(i<len(nums)-1 and nums[i+1]!=0):
        #             nums[i]=nums[i+1]
        #             nums[i+1]=0
        #             i+=1
        i=0
        for j in range(len(nums)):
            if(nums[j]!=0):
                nums[i]=nums[j]
                i+=1
        for j in range(len(nums)-1,i-1,-1):
            nums[j]=0