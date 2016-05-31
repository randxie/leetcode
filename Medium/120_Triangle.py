class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        minimum={0:0}
        for i in range(len(triangle)):
            tmpele=triangle[i]
            tmpminimum=minimum.copy()
            for j in range(len(triangle[i])):
                if j==0:
                    minimum[j]=tmpminimum[j]+tmpele[j]
                elif j==(len(triangle[i])-1):
                    minimum[j]=tmpminimum[j-1]+tmpele[j]
                else:
                    minimum[j]=min(tmpminimum[j-1],tmpminimum[j])+tmpele[j]
        return (minimum[min(minimum,key=minimum.get)])