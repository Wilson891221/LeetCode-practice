class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        count2 = 0
        if len(nums)==1:
            return nums[0]
        for i in range(pow(2,23)-1):
            count = 0
            count2 = 0
            for j in range(len(nums)):
                if nums[j] == i:
                    count+=1
                if (nums[j]*-1) == i:
                    count2+=1
            if count> math.floor(len(nums)/2):
                return i
            if count2> math.floor(len(nums)/2):
                return i*-1