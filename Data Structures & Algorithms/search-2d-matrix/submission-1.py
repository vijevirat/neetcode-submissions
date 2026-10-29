class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0 
        i, j = 0, len(matrix[0]) - 1
        c = len(matrix) - 1

        while r <= c:
            m = (r+c)//2
            if matrix[m][0] == target:
                return True
            if matrix[m][0]<target<=matrix[m][-1]:
                c = m
                break
            elif matrix[m][0]<target:
                r = m + 1
            else:
                c = m - 1
        while i <= j:
            m = (i+j)//2
            if matrix[c][m] == target:
                return True
            if matrix[c][m] < target:
                i = m+1
            else:
                j = m-1
        return False

            
