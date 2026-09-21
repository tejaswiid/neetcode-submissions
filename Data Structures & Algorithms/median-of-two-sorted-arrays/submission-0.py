class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        target = total // 2 + 1
        res = []
        
        while len(res) < target:
            if nums1 and nums2 and nums1[0] < nums2[0]:
                res.append(nums1[0])
                nums1 = nums1[1:]
            elif nums1 and nums2:
                res.append(nums2[0])
                nums2 = nums2[1:]
            elif nums1 and not nums2:
                res.append(nums1[0])
                nums1 = nums1[1:]
            elif nums2 and not nums1:
                res.append(nums2[0])
                nums2 = nums2[1:]
            else:
                break
        # print(res)
        return res[-1] if total % 2 else (res[-1] + res[-2]) / 2



        