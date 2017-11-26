class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxval = 0
        count = 0
        
        for x in nums:
            if x == 1:
                count += 1
            else:
                if maxval < count:
                    maxval = count
                count=0

        if maxval < count:
            maxval = count

        return  maxval