class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1 = 0
        p2 = 0
        ans = []

        while p1 <= m-1 and p2 <= n-1:

            if nums1[p1] < nums2[p2]:
               ans.append(nums1[p1])
               p1 += 1
            else:
                ans.append(nums2[p2])
                p2 += 1
            
        while p1 <= m-1:

            ans.append(nums1[p1])
            p1 += 1
        
        while p2 <= n-1:
            ans.append(nums2[p2])
            p2 += 1
            
        nums1[:] = ans
  
            


