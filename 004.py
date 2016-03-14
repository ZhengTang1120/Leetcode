class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        def findkth(nums1,nums2,k):
            m = len(nums1)
            n = len(nums2)
            if m > n:
                return findkth(nums2,nums1,k)
            if m == 0:
                return float(nums2[k-1])
            if k == 1:
                return float(min(nums1[0],nums2[0]))
            pa = min(k/2,m)
            pb = k-pa
            if (nums1[pa - 1] < nums2[pb - 1]): 
                return findkth(nums1[pa:],nums2, k - pa);  
            elif (nums1[pa - 1] > nums2[pb - 1]):  
                return findkth(nums1,nums2[pb:], k - pb);  
            else: 
                return float(nums1[pa - 1]);
                
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total%2 == 1:
            return findkth(nums1,nums2,total/2+1)
        else:
            return (findkth(nums1,nums2,total/2+1)+findkth(nums1,nums2,total/2))/2