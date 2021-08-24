class Solution:
    def generate(self, row: int) -> List[List[int]]:
        if row == 1:
            return [[1]]
        if row == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(2,row):
            temp = []
            for j in range(i+1):
                if j == i or j == 0:
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(temp)
        return ans
        
               
            