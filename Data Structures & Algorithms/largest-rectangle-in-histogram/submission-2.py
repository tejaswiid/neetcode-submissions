class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = max(heights)
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height*(i-index))
                start = index
            stack.append([start,h])
        n = len(heights)
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height*(n-index))
        return max_area

        