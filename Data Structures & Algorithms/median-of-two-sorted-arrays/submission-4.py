class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2 
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A

        l, r = 0, len(A)
        while True:
            m = (l+r) // 2
            mi = half - m 
            Aleft = A[m-1] if m > 0 else float("-inf")
            Aright = A[m] if m <= len(A) - 1 else float("inf")
            Bleft = B[mi-1] if mi > 0 else float("-inf")
            Bright = B[mi] if mi <= len(B) - 1 else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright,Bright)
                else:
                    return (min(Aright,Bright) + max(Aleft,Bleft)) / 2
            elif Bleft > Aright:
                l = m + 1
            elif Aleft > Bright:
                r = m - 1
        



        
        


        