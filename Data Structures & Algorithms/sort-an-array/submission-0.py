class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        l = self.sortArray(nums[:mid])
        
        r = self.sortArray(nums[mid:])

        return slef.merge(l,r)

    def merge(self,l,r):

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                a.append(left[i])
                i += 1

            else:

                a.append(right[j])
                j += 1

        while i < len(left):

            a.append(left[i])
            i += 1

        while j < len(right):

            a.append(right[j])
            j += 1

        return a 
        
        