class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

##################################### 
#   Data Structure: Strings
#   Algorithm: Two Pointers
#   Problem: Valid Palindrome
#   Difficulty: Easy
#####################################
# Big O
# Time complexity: O(n) since we traverse the string only once in the worst case.
# Space complexity: O(1) since we are using only a constant amount of space and not storing any data in memory.

# ---THE PROBLEM---

# Given a string, determine if it is a valid palindrome, considering only alphanumeric characters
# and ignoring cases. A valid palindrome reads the same backward as forward.

# ---MY EXPLANATION---

# The idea is to use two pointers, one starting at the beginning of the string and the other at the end.
# We move the pointers inward, skipping non-alphanumeric characters, and compare the characters at these
# pointers after converting them to lowercase. If they are not equal at any point, we return False.
# If we reach a point where pointers overlap (same index), it means the string is a valid palindrome, and we return True.