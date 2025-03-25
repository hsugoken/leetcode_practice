class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #   L   R
        #T#[1 2 3]    #[7 4 1]
        # #[4 5 6] => #[8 5 2]
        #B#[7 8 9]    #[9 6 3]
        l = 0
        r = len(matrix[0])-1
        while l<r:
            for i in range(r-l):
                #print(i)
                top, bottom = l, r
                topleft = matrix[top][l+i]
                #move to top left from bottom left
                matrix[top][l+i] = matrix[bottom-i][l]
                #move to bottom left from bottom right
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #move to bottom right from top right
                matrix[bottom][r-i] = matrix[top+i][r]
                #move to top right from top left
                matrix[top+i][r] = topleft
        
            l+=1
            r-=1
        
