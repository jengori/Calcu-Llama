from decimal import Decimal

operators = ['+', '-', '*', '/']


def token_list(exp: str) -> list:
    """converts a sum string to a list of the tokens in the sum, e.g. '2+10' -> ['2', '+', '10']"""

    tokenized_exp = ''

    for i in range(len(exp) - 1):
        if exp[i].isnumeric() or exp[i] == '.':
            if exp[i+1].isnumeric() or exp[i+1] == '.':
                tokenized_exp += exp[i]
            else:
                tokenized_exp += exp[i] + ' '

        else:
            tokenized_exp += exp[i] + ' '

    tokenized_exp += exp[-1]
    tokens = tokenized_exp.split()

    return tokens


def convert(exp: str) -> str:
    """converts a sum string in infix notation to a sum string in Reverse Polish Notation, e.g. '2+10' -> '2 10 +' """
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = ''

    tokens = token_list(exp)

    for token in tokens:
        if token not in operators:

            if token == '(':
                stack.append('(')

            elif token == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop() + ' '

                stack.pop()

            else:
                output += token + ' '

        else:
            while stack and stack[-1] != '(' and priority[token] <= priority[stack[-1]]:
                output += stack.pop() + ' '
            stack.append(token)

    while stack:
        output += stack.pop() + ' '

    return output


def evaluate(exp: str):
    """takes a sum string in infix notation and returns a numerical value of decimal type"""
    exp = convert(exp)
    exp = exp.split()
    stack = []

    for char in exp:
        if char not in '+-*/^':
            stack.append(Decimal(char))

        else:
            right_operand = stack.pop()
            left_operand = stack.pop()

            if char == '+':
                stack.append(left_operand + right_operand)

            elif char == '-':
                stack.append(left_operand - right_operand)

            elif char == '*':
                stack.append(left_operand * right_operand)

            elif char == '/':
                stack.append(left_operand / right_operand)

    return stack.pop()
