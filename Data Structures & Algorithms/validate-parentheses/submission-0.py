class Solution:
    def isValid(self, s: str) -> bool:
        b_map = {')': '(', '}': '{', ']': '['}

        stack =[]
        for char in s:
            if char in b_map:

                t_e = stack.pop() if stack else '#'

                if b_map[char] != t_e:
                    return False
            else:
                stack.append(char)

        return not stack