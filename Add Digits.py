class Solution(object):
    def addDigits(self, num):
        ans = num % 9
        if num != 0 and ans==0:
            ans=9
        return ans
        