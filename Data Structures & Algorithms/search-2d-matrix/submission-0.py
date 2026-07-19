class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMN = len(matrix), len(matrix[0])
        top, bottom = 0 , ROWS - 1
        while top <= bottom:
            mrow = (top + bottom) // 2
            if target > matrix[mrow][-1]:
                top = mrow + 1
            elif target < matrix[mrow][0]:
                bottom = mrow - 1
            else:
                break

        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        l , r = 0 , COLUMN - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

                