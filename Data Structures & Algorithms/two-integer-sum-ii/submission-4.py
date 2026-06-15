class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)

        l = 0
        r = n-1

        while l <= r:

            need = numbers[l] + numbers[r]

            if need == target:
                return [l+1,r+1]
            elif need > target:
                r -= 1
            else:
                l+=1            