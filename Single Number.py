class Solution:
    def singleNumber(self, num: List[int]) -> int:
        temp = 0 
        for i in range(len(num)):
            temp ^= num[i]
        return temp
                