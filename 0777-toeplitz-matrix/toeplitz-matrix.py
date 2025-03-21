class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        def traverse_diagnol(r,c):
            curr = matrix[r][c]
            while 0<=r<ROW and 0<=c<COL:
                if matrix[r][c]!=curr:
                    return False
                r += 1
                c += 1
            return True
        
        for r in range(ROW):
            # c = 0
            if not traverse_diagnol(r,0):
                return False
        for c in range(1,COL):
            if not traverse_diagnol(0,c):
                return False
        return True

        
