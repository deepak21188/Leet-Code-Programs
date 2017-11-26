class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j,ans=0,0,0
        dict = {}
        for j in range(len(s)):
            if( (s[j] in dict) and (i <= dict[s[j]]) ):
                i=dict[s[j]]+1
            dict[s[j]] = j
            ans= max(ans,j-i+1)

        return ans
