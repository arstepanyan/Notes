"""
Write a program that takes an arithmetic expression in RPN and returns the number that the expression evaluates to.
For example, "3,4,+,2,X,1,+" evaluates to 15 because (3+4)*2+1=15
"""

# Recursive solution
def rpn_to_int(s):
    s_list = s.split(',')
    return _rpn_to_int(s_list)

def _rpn_to_int(s_list):
    if len(s_list) == 1:
        return int(s_list[0])

    if s_list[-1] == '+':
        return _rpn_to_int(s_list[:len(s_list)-2]) + int(s_list[-2])
    elif s_list[-1] == '-':
        return _rpn_to_int(s_list[:len(s_list)-2]) - int(s_list[-2])
    elif s_list[-1] == 'x':
        return _rpn_to_int(s_list[:len(s_list)-2]) * int(s_list[-2])
    elif s_list[-1] == '/':
        return int(_rpn_to_int(s_list[:len(s_list)-2]) / int(s_list[-2]))



# Using stack
def rpn_to_int2(s):
    intermediate_results = []
    operators = {'+': lambda y, x: x + y,
                 '-': lambda y, x: x - y,
                 'x': lambda y, x: x * y,
                 '/': lambda y, x: int(x / y)}

    for token in s.split(','):
        if token in operators:
            intermediate_results.append(operators[token](intermediate_results.pop(), intermediate_results.pop()))
        else: # token is a number
            intermediate_results.append(int(token))
    return intermediate_results[-1]


if __name__ == '__main__':
    rpn = '3,4,+,2,x,1,+'
    print(rpn_to_int(rpn), rpn_to_int(rpn) == rpn_to_int2(rpn))

    rpn = '1729'
    print(rpn_to_int(rpn), rpn_to_int(rpn) == rpn_to_int2(rpn))

    rpn = '1,1,+,-2,x'
    print(rpn_to_int(rpn), rpn_to_int(rpn) == rpn_to_int2(rpn))

    rpn = '-641,6,/,28,/'
    print(rpn_to_int(rpn), rpn_to_int(rpn) == rpn_to_int2(rpn))
