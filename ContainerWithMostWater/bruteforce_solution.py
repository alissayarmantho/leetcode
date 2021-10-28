class Solution:
    def maxArea(self, height: List[int]) -> int:
        list_length = len(height)
        max_area = 0
        for i in range (0, list_length):
            curr_height = height[i]
            for j in range (list_length - 1 , -1, -1):
                if height[j] >= curr_height:
                    curr_area = abs((j- i)) * curr_height
                    if curr_area > max_area:
                        max_area = curr_area
        last_height = height[list_length - 1]
        return max_area
