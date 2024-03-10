class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newnums=nums1+nums2
        newnums.sort()
        # print(newnums)
        l=len(newnums)
        if l%2!=0:
            return(newnums[l//2]/1.0)
        else:
            return((newnums[l//2]+newnums[(l//2)-1])/2.0)