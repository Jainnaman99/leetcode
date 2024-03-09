class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sort_l=sorted(nums)
        # print (sort_l[0],sort_l[1],sort_l[len(nums)-2],sort_l[len(nums)-1])
        return((sort_l[len(nums)-2]*sort_l[len(nums)-1])-(sort_l[0]*sort_l[1]))