class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0, r = len(height)-1
        max_height = 0
        while r != l:
            if height[r] >= height[l]:
                curr_height = height[l] * (r-l)
                l += 1
            else:
                curr_height = height[r] * (r-l)
                r -= 1
            if curr_height > max_height:
                max_height = curr_height
            
        return max_height

##################################### 
#   Data Structure: Array (List)
#   Algorithm: Two Pointers
#   Problem: Container With Most Water
#   Difficulty: Medium
#####################################
# Big O
# Time complexity: O(n) since we traverse the list only once in the worst case
# Space complexity: O(1) since we are using only a constant amount of space and not storing any data in memory

# ---THE PROBLEM---

# Find two lines (bars) in a given list of heights that can form a container
# with the maximum area of water that can be contained between them. Each line is represented
# by its height, and the width between the two lines is determined by their indices in the list

# ---MY EXPLANATION---

# The idea is to use two pointers, one at the beginning and one at the end of the array.
# We calculate the area formed by the lines at these two pointers and move the pointer
# that points to the shorter line inward (since we are looking to maximize area), 
# hoping to find a taller line that could potentially
# form a larger area. We repeat this process until the two pointers meet.