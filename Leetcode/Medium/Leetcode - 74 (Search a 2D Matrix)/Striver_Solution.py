class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = (m * n) - 1
        while low <= high:
            mid = (low + high) // 2
            row = int(mid // n)
            col = int(mid % n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                    low = mid + 1
            else:
                high = mid - 1
        return False
