class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = 0

        while n < len(matrix):

            l = 0
            r = len(matrix[n])-1

            while l <= r:

                mid = (l+r) // 2

                if matrix[n][mid] == target:
                    return True
                elif matrix[n][mid] < target:
                    l = mid +1
                else:
                    r = mid-1
                
            n +=1
        
        return False