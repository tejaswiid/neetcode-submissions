class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(list)
        for i,n in enumerate(nums):
            count[n].append(i)
        # print(count)
        for key,arr in count.items():
            if len(arr) > 1:
                # print(arr)
                for i in range(1,len(arr)):
                    if abs(arr[i]-arr[i-1]) <= k:
                        return True
        return False

        