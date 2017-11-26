class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        outlist = []
        flag=0
        for j,x in enumerate(findNums):
            i=nums.index(x)
            for y in nums[i+1:len(nums)]:
                if y>x :
                    outlist.append(y)
                    break
            if j+1 != len(outlist):
                outlist.append(-1)
        return  outlist