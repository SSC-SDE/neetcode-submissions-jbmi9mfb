class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        # Check if the filtered string is equal to its reverse
        return filtered_s == filtered_s[::-1]