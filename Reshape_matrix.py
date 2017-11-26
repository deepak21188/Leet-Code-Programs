class Solution(object):
    def matrixReshape(self, nums, r, c):
        matSize1 = len(nums)*len(nums[0])
        matSize2 = r*c
        k=0
        temp = []
        result = []

        if matSize1 == matSize2:
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    temp.append(nums[i][j])
                    k+=1
            k=0
            for i in range(r):
                result.append([])
                for j in range(c):
                    result[i].append(temp[k])
                    k+=1
            return result
        else:
            return nums
      