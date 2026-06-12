class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        mp = {}

        for i,num in enumerate(nums):

            t = target - num

            if t in mp:
                return[mp[t],i]

            mp[num] = i