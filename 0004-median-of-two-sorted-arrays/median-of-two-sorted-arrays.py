class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        #swap if B is smaller
        if len(B)<len(A):
            A, B = B,A
        
        left, right = 0, len(A) - 1
        # If we need 'half' elements in right side
        # And we took (i+1) elements from A for left side
        # Then from total elements (j+1) we want from B:
        # half = (i + 1) + (j + 1)
        # j + 1 = half - (i + 1)
        # j = half - i - 2
        while True:
            i = (left+right)//2 #gives the paritition point in A
            j = half - i -2 # partition point in j

            #check bounds here
            #If i < 0: no elements in left partition of A
            #If i + 1 ≥ len(A): no elements in right partition of A
            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if (i+1)<len(A) else float('inf')

            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if (j+1)<len(B) else float('inf')

            #check validitiy of partition
            if Aleft<=Bright and Bleft<=Aright:
                #do median calculation
                #if odd
                if total%2:
                    #For odd length: return smallest right element
                    return min(Aright, Bright)
                else:
                    #For even length: average of largest left and smallest right
                    return (min(Aright, Bright)+max(Aleft, Bleft))/2
            #invalid parititon
            elif Aleft>Bright: #took too many elements from A
                right = i - 1
            else: #checks for Bleft>=Aright
                #take few elements from A
                left = i + 1

