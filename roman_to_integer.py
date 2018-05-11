class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt={
          "I":1,
          "V":5,
          "X":10,
          "L":50,
          "C":100,
          "D":500,
          "M":1000
        }
        sum=0
        i=0
        while i < len(s):
          num=dt[s[i]]
          if i != len(s)-1:
            if s[i]=="I" and (s[i+1] == "V" or s[i+1] == "X"):
              num=dt[s[i+1]]-dt[s[i]]
              i=i+1
            elif s[i]=="X" and (s[i+1] == "L" or s[i+1] == "C"):
              num=dt[s[i+1]]-dt[s[i]]
              i=i+1
            elif s[i]=="C" and (s[i+1] == "D" or s[i+1] == "M"):
              num=dt[s[i+1]]-dt[s[i]]
              i=i+1
          sum=sum+num
          i+=1
          
        return sum

sl=Solution()
sl.romanToInt("MCMXCIV")