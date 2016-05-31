class Solution(object):
    def subsets(self, nums):
        tot_sub = []
        if (len(nums)==0):
            return []
        s = nums[0]
        residual = list(nums)
        residual.remove(s)
        nsub = self.subsets(residual)
        tot_sub.append(nsub)
        tot_sub.append(self.addElement(s,nsub))
        if (len(nums)>=2):
            tot_sub = tot_sub[0] + tot_sub[1]
        return tot_sub
    
    def addElement(self,s,nsub):
        tmp = list(nsub)
        if (len(tmp)==0):
            return [s]
        elif (len(tmp)==1):
            return tmp + [s]
        for i in range(len(tmp)):
            tmp[i] = sorted (tmp[i] + [s])
        return tmp