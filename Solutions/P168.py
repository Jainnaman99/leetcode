class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=''
        while(columnNumber>0):
            rem=(columnNumber-1)%26
            result=chr(65+rem)+result
            columnNumber=(columnNumber-1)//26
        return result