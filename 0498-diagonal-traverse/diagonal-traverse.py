class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        going_up = True
        ROW = len(mat)
        COL = len(mat[0])
        res = []
        r,c = 0,0
        while len(res)!=ROW*COL:
            if going_up:
                while 0<=r<ROW and 0<=c<COL:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
                if c>=COL:
                    r+=2
                    c-=1
                else:
                    r+=1
                going_up = False
            else:
                while 0<=r<ROW and 0<=c<COL:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
                if r>=ROW:
                    c += 2
                    r -= 1
                else:
                    c += 1
                going_up = True
        return res

