class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        for first in xrange(len(numbers)):
            b = first+1
            e = len(numbers)-1
            while(b<=e):
                mid = (b+e)/2
                if numbers[first]+numbers[mid]==target:
                    return [first+1,mid+1]
                elif  numbers[first]+numbers[mid] > target:
                    e = mid - 1
                else:
                    b = mid + 1