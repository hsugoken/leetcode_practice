class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = l + (r-l)//2
            missing_nos = arr[mid]-(mid+1)
            if missing_nos<k:
                #
                l = mid + 1
            else:
                r = mid - 1
            
        missing_current = arr[r]-r
        missing_remaining = k-missing_current
        #k-arr[r]+r + arr[r] + 1
        return k + l

        