class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        maxArea = 0
        for i in range(len(heights)):
            cs = i
            while st and heights[i] < st[-1][1]:
                a, b = st.pop()
                temp = (i-a)*b
                maxArea = max(maxArea, temp)
                cs = a
            st.append((cs, heights[i]))
        while st:
            a, b = st.pop()
            maxArea = max(maxArea, (len(heights)-a)*b)
        return maxArea