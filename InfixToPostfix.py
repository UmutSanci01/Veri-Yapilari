def infixToPostfix(infix: str) -> str:
    operators = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    result = []

    s = infix.replace(' ', '') # bosluklar temizlendi
    for c in s:
        if c == '(':
            stack.append(c)
            
        elif c == ')': # ac parantez gorunceye kadar stack'i sonuca bosalt
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack: # ac parantezi cope at
                stack.pop() 
                
        elif c in operators:
            # eger stack'in en tepesindeki operator mevcuttan buyuk veya esit oncelikteyse
            # bu kosul saglandigi surece stack'i sonuca bosalt
            while stack and stack[-1] in operators and operators[stack[-1]] >= operators[c]:
                result.append(stack.pop())
            
            stack.append(c)
            
        else:
            result.append(c)

    # stack'de kalanlari da sonuca bosalt
    while stack:
        result.append(stack.pop())

    return " ".join(result)

if __name__ == "__main__":
    print(infixToPostfix("(A + B) * (C - D)"))
    print(infixToPostfix("A + B * C / D"))
    print(infixToPostfix("A + B"))
    print(infixToPostfix("A + B * C"))
    print(infixToPostfix("A - B - C"))
    print(infixToPostfix("A + B * C / D - E"))