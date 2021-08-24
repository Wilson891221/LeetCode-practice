class Solution:
    def getRow(self, row: int) -> List[int]:
        if row == 0:
            return [1]
        if row == 1:
            return [1,1]
        temp = [1,1]
        ans = []
        for i in range(2,row+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    ans.append(1)
                else:
                    ans.append(temp[j]+temp[j-1])
            temp = ans
            ans = []
        return temp