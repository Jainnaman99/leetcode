class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        sum=0
        s2=0
        for i in range(1,n+1):
            sum+=i
        # print (sum)
        for i in range(n,0,-1):
            # print(i)
            s2+=i  #0  8  15 21
            sum-=i #36 28 21 15
            if(s2>sum and s2==sum+i):
                return i

        return -1
