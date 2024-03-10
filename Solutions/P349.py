# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         l1=[]
#         for i in nums1:
#             if i in nums2:
#                 l1.append(i)
#         return(set(l1))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1 - (set1 - set2))