class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftp,rightp=1,1
        l1=[]
        l2=[]
        res=[0]*len(nums)
        l1.append(1)
        l2.append(1)
        for i in range(1,len(nums)):
            leftp*=nums[i-1]
            l1.append(leftp)
        print(l1)
        for i in range(len(nums)-1,0,-1):
            rightp*=nums[i]
            l2.append(rightp)
        l2.reverse()
        print(l2)
        for i in range(len(nums)):
            res[i]=l1[i]*l2[i]
        return res