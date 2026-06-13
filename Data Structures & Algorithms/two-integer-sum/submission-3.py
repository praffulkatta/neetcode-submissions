class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        mp = {}

        for num in nums:

            needed = target - num

            if needed in mp:
                return [mp[num], num]
            
        return [-1,-1]