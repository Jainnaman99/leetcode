class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[0,0]
        n1=set(nums1)
        n2=set(nums2)
        # print(n1)
        ans[0]=n1-n2
        ans[1]=n2-n1
        return ans