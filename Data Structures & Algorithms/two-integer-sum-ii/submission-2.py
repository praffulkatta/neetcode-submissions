class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        l = 0
        r = n -1

        while l <= r:

            curr = numbers[l] + numbers[r]

            if curr == target:
                return [l,r]
            elif curr > target:
                r  -= 1
            else:
                l += 1
            