class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        mp = {}

        for num in nums:

            needed = target - num

            if need in mp:
                return [mp[need], num]
            
        return [-1,-1]