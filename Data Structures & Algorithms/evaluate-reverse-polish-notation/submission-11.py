class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a dictionary of equations
        def sub(x,y):
            return x - y
        def add(x,y):
            return x + y
        def mul(x,y):
            return x * y
        def div(x,y):
            return int(x / y)

        eqs = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
        }

        stack = []
        for token in tokens:
            if token in eqs:
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(str(eqs[token](x, y)))
            else:
                stack.append(token)
        return int(stack[0])