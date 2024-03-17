class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=maxans=0
        for i in gain:
            ans+=i
            maxans=max(ans,maxans)
        return maxans