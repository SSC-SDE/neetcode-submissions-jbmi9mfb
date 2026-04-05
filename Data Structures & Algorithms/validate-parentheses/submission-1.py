class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap = {")" : "(" , "}" : "{", "]":"["}
        for c in s:
            if c in hashmap:
                b = stack.pop() if stack else '#'
                if hashmap[c] != b:
                    return False
            else:
                stack.append(c)
        return not stack


