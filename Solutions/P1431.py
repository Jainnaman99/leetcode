class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_a=sorted(candies,reverse=True)
        mx=new_a[0]
        l1=[None]*len(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=mx):
                l1[i]=True
            else:
                l1[i]=False
        # print(new_a)
        return l1
