class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec1d = []
        for i in xrange(len(vec2d)):
            for j in xrange(len(vec2d[i])):
                self.vec1d.append(vec2d[i][j])

    def next(self):
        """
        :rtype: int
        """
        temp = self.vec1d[0]
        self.vec1d = self.vec1d[1:]
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.vec1d) >= 1:
            return True
        else:
            return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())