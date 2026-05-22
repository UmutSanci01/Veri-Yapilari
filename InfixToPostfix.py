def infixToPostfix(infix : str) -> str:
    operators = "*/+-)"

    stack = []
    result = ""

    for c in infix:
        if c == ')':
            result += ' ' + (' '.join(stack))[::-1]
            stack.clear()
        elif len(stack) > 0 and operators.find(stack[-1]) <= operators.find(c):
            result += ' ' + (' '.join(stack))[::-1]
            stack.clear()
            stack.append(c)
        elif c in operators:
            stack.append(c)
        elif c != '(':
            result+=c

    result += ' ' + (' '.join(stack))[::-1]

    return result

print(infixToPostfix("(A + B) * (C - D)"))
print(infixToPostfix("A + B * C / D"))
print(infixToPostfix("A + B"))
print(infixToPostfix("A + B * C"))
print(infixToPostfix("A - B - C"))
print(infixToPostfix("A + B * C / D - E"))