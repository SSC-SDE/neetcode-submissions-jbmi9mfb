import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmerd_s = re.sub(r'[^a-zA-Z0-9]','',s).lower()

        return trimmerd_s == trimmerd_s[::-1]
        