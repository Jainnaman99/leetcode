class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # d={}
        # for i in nums:
        #     if(i in d):
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # for i in d:
        #     if d[i]>1:
        #         return i
        # return 0
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)