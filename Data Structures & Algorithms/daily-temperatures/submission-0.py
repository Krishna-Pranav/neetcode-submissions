class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        st = []
        for i, temp in enumerate(temperatures):
            if len(st) == 0 or st[-1][1] > temp:
                st.append((i, temp))
            else:
                while st and st[-1][1] < temp:
                    a, b = st.pop()
                    result[a] = i-a
                st.append((i, temp))
        return result