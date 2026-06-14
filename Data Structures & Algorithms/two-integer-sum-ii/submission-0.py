class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        l = 0
        r = n -1

        while l <= r:

            mid = (l+r)//2

            if (mid + l) == target:
                return [l,mid]
            elif (mid + l) > target:
                r = mid -1
            else:
                l = mid +1
            