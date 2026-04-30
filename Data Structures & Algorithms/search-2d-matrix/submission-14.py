class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for the row where, the end element
        # step 1: finding the right row
        t, b = 0, len(matrix) - 1
        row = None
        while t <= b:
            m = (t+b) // 2
            print(matrix[m])
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row = matrix[m]
                break
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1

            print()

        if row is None:
            return False

    
        left, right = 0, len(row) - 1
        while left <= right:
            m = (left + right) // 2
            print(row[m], target)
            if row[m] == target:
                return True
            elif row[m] > target:
                right = m - 1
            else:
                left = m + 1
        
        return False
            