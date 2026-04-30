class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(x,y):
            return x+y
        def sub(x,y):
            return x-y
        def mul(x,y):
            return x*y
        def div(x,y):
            return int(x/y)
        stack = []
        operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
        }
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                result = operations[token](x,y)
                stack.append(result)
        return stack[0]
        