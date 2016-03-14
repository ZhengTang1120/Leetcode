class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.rank = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.rank:
            self.rank.remove(key)
            self.rank.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.rank:
            self.rank.append(key)
        else:
            self.rank.remove(key)
            self.rank.append(key)
        self.cache[key] = value
        if len(self.rank) > self.capacity:
            self.rank = self.rank[1:]
            
        