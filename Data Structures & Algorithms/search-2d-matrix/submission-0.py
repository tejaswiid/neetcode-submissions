class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
 
        rows =  len(matrix)
        l, r = 0, rows - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                if target in matrix[m]: 
                    return True
                else: return False
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
        return False


                    

        