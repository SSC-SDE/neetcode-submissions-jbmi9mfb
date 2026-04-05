from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter '#'
            j = s.find('#', i)
            length = int(s[i:j])  # Extract the length of the next word
            i = j + 1  # Move past the '#'
            res.append(s[i:i+length])  # Extract the word
            i += length  # Move to the next encoded string
            
        return res
