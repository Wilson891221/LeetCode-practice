class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while(k):
            temp = (min(nums))
            nums[nums.index(temp)] *= -1
            k -=1
        return sum(nums)