class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # s1=set(nums1)
        # s2=set(nums2)
        # # l1=s1[len(s1)-1]
        # # # print(l1)
        # # l2=s2[len(s2)-1]
        # # # print(l2)
        # # end=min(l1,l2)
        # l1=[]
        # for i in s1:
        #     if(i in s1 and i in s2):
        #         l1.append(i)
        # if(len(l1)!=0):
        #     l1.sort()
        #     return l1[0]
        # return -1
        s1=set(nums1)
        for i in nums2:
            if i in s1:
                return i
        return -1