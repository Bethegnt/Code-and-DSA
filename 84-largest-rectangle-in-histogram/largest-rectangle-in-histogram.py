class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights = heights+[0]
        n = len(heights)
        for i in range(n):
            height = heights[i]
            stack_idx = i
            while stack and stack[-1][0] >= height:
                stack_height, stack_idx = stack.pop()
                w = i - stack_idx
                res = max(res,(w*stack_height))
            stack.append((height,stack_idx))
        return res