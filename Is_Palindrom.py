class Solution(object):
    def isPalindrome(self, x):
        count=0
        n=x
        if(n<0):
            return False
        if(x== 0):
            return True
        while(n>0):
            n=n/10
            count+=1
        i= count-1
        j=0
        if(count == 1):
            return True

        for k in range(count/2):
            if( (x/(10**i))%10 != (x/(10**j))%10 ):
                return False
            i-=1
            j+=1

        return True