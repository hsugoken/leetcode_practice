class SparseVector:
    def __init__(self, nums: List[int]):
        #[1,0,0,0,0,1]
        self.pair = []
        for i,n in enumerate(nums):
            if n:
                self.pair.append([i,n])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.pair
        v2 = vec.pair

        i = j = 0 #i is index for vector 1
        #j is index for vector 2
        res = 0

        while i<len(v1) and j<len(v2):
            idx1, val1 = v1[i][0], v1[i][1] 
            idx2, val2 = v2[j][0], v2[j][1]
            #[[2,3]]
            #[[1,1],[2,3],[3,3]]
            if idx1==idx2:
                res += val1*val2
            if idx1<idx2:
                i+=1
            else:
                j+=1
        return res
#TC: dotProduct: O(min(#non-zero elements in vec1 and vec2)) / O(N) __init__ => O(N)
#SC: O(N)
#Let n be the length of input array and L and L2 be the number of non-zero 
#elements for the two vectors
#TC: O(n) for creating the <index, value> pair for non-zero values and 
#O(L+L2) for calculating the dot product

#SC: O(L) for <index,value> pairs and O(1) for dot product
            

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)