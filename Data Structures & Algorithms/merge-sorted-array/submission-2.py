class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1.copy()[:m]
        n1 += nums2
        n1.sort()
        for i in range(m+n):
            nums1[i] = n1[i]
            