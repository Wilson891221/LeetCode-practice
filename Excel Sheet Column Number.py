class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            temp = pow(26,len(columnTitle)-1-i)*(ord(columnTitle[i])-ord('A')+1)
            ans+=temp
        return ans