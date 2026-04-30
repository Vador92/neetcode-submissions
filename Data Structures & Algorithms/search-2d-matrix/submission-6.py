class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            m = (left + right) // 2
            if target in set(matrix[m]):
                return True
            elif target < matrix[m][-1]:
                right = m - 1
            else:
                left = m + 1 
        return False