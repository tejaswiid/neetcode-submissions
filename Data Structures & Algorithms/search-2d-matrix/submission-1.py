class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binn(row):
            l, r = 0, len(row) - 1
            while l <= r:
                m = (l+r) // 2
                if row[m] > target:
                    r = m - 1
                elif row[m] < target:
                    l = m + 1
                else:
                    return True
            return False
        rows =  len(matrix)
        l, r = 0, rows - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return binn(matrix[m])
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
        return False


                    

        