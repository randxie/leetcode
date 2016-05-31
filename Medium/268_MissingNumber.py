class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)
        if nums[0]!=0:
            return 0
            
        if len(nums)==1:
            if nums[0]==1:
                return 0
            else:
                return 1
                
        for i in range(0,len(nums)-1):
            if nums[i+1]!=(nums[i]+1):
                return (nums[i]+1)
        return nums[-1]+1
        """
        :type nums: List[int]
        :rtype: int
        """