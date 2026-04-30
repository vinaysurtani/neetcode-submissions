class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()
        l = 0
        r = len(nums1) - 1
        m1 = (l+r)//2
        m2 = math.ceil((l+r)/2)
        print(m1, m2)
        if len(nums1) % 2 == 1:
            return nums1[m1]
        else:
            return (nums1[m1] + nums1[m2])/ 2