from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                # Pop the top two elements from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation based on the token
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    # Perform integer division that truncates towards zero
                    result = int(a / b)  # Using int() to truncate towards zero
                
                # Push the result back onto the stack
                stack.append(result)
            else:
                # If the token is a number, convert it to an integer and push onto the stack
                stack.append(int(token))
        
        # The final result will be the only element left in the stack
        return stack[0]

# Example usage:
solution = Solution()
tokens = ["1", "2", "+", "3", "*", "4", "-"]
output = solution.evalRPN(tokens)
print(output)  # Output: 5