class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        a=sorted(nums)
        for i in range(0,len(a)-1):
          if a[i] == a[i+1]:
            return True
        
        return False
      