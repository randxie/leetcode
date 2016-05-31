class Solution:
    # @param {integer[]} nums
    # @return {integer}
    past={}
    def rob(self, nums):
        if not nums:
            return 0
        past={}
        past['0']=0
        past['1']=nums[0]
        curr=past
        for iter in range(1,len(nums)):
            curr={}
            if past['1']>past['0']:
                curr['0']=past['1']
            else:
                curr['0']=past['0']
            curr['1']=past['0']+nums[iter]
            past=curr
        return curr[max(curr, key=curr.get)]