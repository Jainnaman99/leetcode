class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i] +=1
        for i in d:
            if d[i]==1:
                return i


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         xor = 0
#         for num in nums:
#             xor ^= num
        
#         return xor