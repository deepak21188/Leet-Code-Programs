class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        firstZero=True
        PrevZero=False
        for i in range(len(nums)):
            
            if(nums[i]==0 and firstZero== True):
                zeroIndex=i
                firstZero=False
            if(nums[i]==0):
                PrevZero=True
            
            if(nums[i] !=0 and PrevZero==True):
                nums[zeroIndex]=nums[i]
                nums[i]=0
                zeroIndex += 1
       