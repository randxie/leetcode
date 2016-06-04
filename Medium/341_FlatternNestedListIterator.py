# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        self.gidx = 0
        self.glen = len(nestedList)
        self.nestedList = nestedList
        self.stack = []
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
    def next(self):
        if(len(self.stack)>0):
            nexti = self.stack.pop(0)
            return nexti
        """
        :rtype: int
        """
        
    def hasNext(self):
        if(len(self.stack)>0):
            return True
            
        while(len(self.stack)==0):
            if(self.gidx>=self.glen):
                return False
            else:
                nextInt = self.nestedList[self.gidx]
                if(nextInt.isInteger()):
                    self.gidx = self.gidx + 1
                    self.stack.append(nextInt.getInteger())
                else:
                    # flatten this list to stack
                    self.appendStack(nextInt)
                    self.gidx = self.gidx + 1
        return True

    def appendStack(self, sublist):
        if(sublist.isInteger()):
            self.stack.append(sublist.getInteger())
        else:
            tmplist = sublist.getList()
            if(len(tmplist)==0):
                return
            else:
                for i in range(len(tmplist)):
                    self.appendStack(tmplist[i])
        """
        :rtype: bool
        """
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())