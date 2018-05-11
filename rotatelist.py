class Solution:
  
    def place(self,nums,index,k):
      num=nums[index]
      if (index+k)<len(nums):
        self.place(nums,index+k,k)
      nums[(index+k)%len(nums)]=num
      return nums
  
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
          nums=self.place(nums,i,k)
        print(nums)