from collections import deque

def operation(a, b, c):
    if c == "+":
        return a + b
    if c == '-':
        return a - b
    if c == "*":
        return a * b
    return int(a / b) if a * b > 0 else -(abs(a) // abs(b))

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numStack = deque()
        ans = 0
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                b = numStack[-1]
                numStack.pop()
                a = numStack.pop()
                print(operation(a, b, c))
                numStack.append(operation(a, b, c))
                continue
            numStack.append(int(c))

        return numStack[-1]

print(6 // -120)