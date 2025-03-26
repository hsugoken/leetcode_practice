"""
When we see any number and have count zero we set that number as majority
If we see majority element we increment the count
If not => we decrement the count 
In the end majority element will have maximum count

The algorithm works because the majority element appears more than n/2 times. Even if all other elements cancel out some occurrences of the majority element, there will still be some occurrences left, making it the final candidate.

Q: What if there is no guaranteed majority element?
Answer: We would need a second pass to verify if the candidate actually appears more than n/2 times.

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[1,2,1,3,1]
        #         ^
        #count = 0
        #majority = 1
        #
        majority = 0
        count = 0
        for n in nums:
            if count == 0:
                majority = n
            if majority == n:
                count += 1
            else:
                count -= 1 

        return majority