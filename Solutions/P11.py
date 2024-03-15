class Solution:
    def maxArea(self, height: List[int]) -> int:
        m,mx=0,0
        l,r=0,len(height)-1
        while(l<r):
            m=min(height[l],height[r])*(r-l)
            mx=max(m,mx)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
            
        return mx