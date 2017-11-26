class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i,sum=0,0
        while i< len(nums):
            sum=sum+ nums[i]
            i=i+2
        return sum