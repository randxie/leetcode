class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        maximum=nums[0]
        totsum=range(0,len(nums))
        totsum[0]=maximum
        for i in range(1,len(nums)):
            totsum[i]=max(totsum[i-1]+nums[i],nums[i])
            maximum=max(maximum,totsum[i])
        return maximum