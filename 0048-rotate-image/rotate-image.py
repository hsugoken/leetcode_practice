"""
     L       R
T    0  0 0  0
     0 |0 0| 0
     0 |0 0| 0
B    0  0 0  0
The bars will be the second iteration
L=0, R=3 (R-L)=3

"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        while l<r:
            
            for i in range(r-l):
                #this only works for one outer layer, it is not doing this for all inner
                #layers as it is not moving inwards
                #to move inwards we have to add i
                
                top, bottom = l, r
                #store top left
                top_left = matrix[top][l+i]
                #move bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]
                #move bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                #move matrix top left to matrix top right
                matrix[top+i][r] = top_left
            l += 1
            r -= 1
        return

