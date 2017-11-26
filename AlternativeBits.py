class Solution(object):
    def hasAlternatingBits(self, n):
        prev = 3

        while(n>0):
            curr = n % 2
            if prev == curr :
                return False
            n = n/2
            prev = curr
        return True