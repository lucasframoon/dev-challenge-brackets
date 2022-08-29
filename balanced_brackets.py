#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    stack = []

    for char in brackets:
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return 'NO'
            top_element = stack.pop()
            if not Compare(top_element, char):
                return 'NO'
    if len(stack) != 0:
        return 'NO'
    return 'YES'


def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
