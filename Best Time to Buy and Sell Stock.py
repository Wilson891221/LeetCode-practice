class Solution:
    def maxProfit(self, arr):
        l = 0
        r = 1
        ans = 0
        for r in range(1,len(arr)):
            if arr[r] > arr[l]:
                best = arr[r] - arr[l]
                ans = max(ans,best)
            else:
                l = r
            r+=1
        return ans