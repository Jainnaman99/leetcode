class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec=0
        while(tickets[k]!=0):
            for i in range(len(tickets)):
                if(tickets[i]!=0 and tickets[k]!=0):
                    sec+=1
                    tickets[i]=tickets[i]-1
                    # print(sec,tickets[i])
                elif(tickets[k]==0):
                    return sec
        return sec