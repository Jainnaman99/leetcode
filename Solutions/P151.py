class Solution:
    def reverseWords(self, s: str) -> str:
        string = " ".join(s.split()[::-1])
        return string
    
        # l=[]
        # res=''
        # s1=s.split()
        # # print (s1)
        # for i in s1:
        #     res=i+" "+res
        # return res[:len(res)-1]