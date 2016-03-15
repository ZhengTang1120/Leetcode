class Solution:
  # @param {integer} k
  # @param {integer} n
  # @return {integer[][]}
  def combinationSum3(self, k, n):
    ans = []
    def generater(k,n,p):
        result = []
        if k == 1 and n > p and n < 10:
            return [[n]]
        else:
            for i in range(p+1,10):
                for res in generater(k-1,n-i,i):
                    res.insert(0,i)
                    result.append(res)
            return result
    return generater(k,n,0)