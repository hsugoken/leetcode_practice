class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_seen = "0"
        max_i = -1
        swap_i = swap_j = -1 
        ##swap_i index of number to be swapped on left with index of number to be swapped on right
        for i in reversed(range(len(num))):
            if num[i]>max_seen:
                max_seen = num[i]
                max_i = i
            elif num[i]<max_seen:
                swap_i = i
                swap_j = max_i
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int(''.join(num))

