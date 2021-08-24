class Solution:
    def twoSum(self, arr: List[int], tar: int) -> List[int]:
        f = 0
        b = len(arr)-1
        temp = []
        while(f != b):
            sum = arr[f] + arr[b]
            if(sum > tar):
                b -= 1
                continue
            if(sum < tar):
                f +=1
                continue
            if(sum == tar):
                temp.append(f+1)
                temp.append(b+1)
                return temp