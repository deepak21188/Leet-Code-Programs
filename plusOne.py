class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        carry=1
        while i>=0:
            num=(int)((digits[i]+carry)/10)
            digits[i]=(digits[i]+carry)%10
            carry=num
            i-=1
        if carry == 1:
          digits.insert(0,carry)
        
        return digits
        