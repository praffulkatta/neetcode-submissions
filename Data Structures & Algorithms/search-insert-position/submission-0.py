class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1

        while l <= r:

            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = mid + 1
            else:
                r = mid -1

        return l
