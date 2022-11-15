from tree import BinaryTree, ExpTree
from stack import Stack

operators = {'+', '-', '*', '/', '(', ')', '^'}
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infix_to_postfix(exp):
    s = Stack()
    output = Stack()  # ''
    i = 0
    while i < len(exp):
        char = exp[i]
        if char not in operators:
            n = ''
            while i < len(exp) and exp[i] not in operators:
                n += exp[i]
                i += 1
            output.push(n)  # output += char
        elif char == '(':
            s.push('(')
            i += 1
        elif char == ')':
            while not s.isEmpty() and s.peek() != '(':
                output.push(s.pop())  # output += s.pop()
            s.pop()
            i += 1
        else:
            while not s.isEmpty() and s.peek() != '(' and priority[char] <= priority[s.peek()]:
                output.push(s.pop())  # output += s.pop()
            s.push(char)
            i += 1

    while not s.isEmpty():
        output.push(s.pop()) # output += s.pop()

    return output


def calculate(exp):
    exp = infix_to_postfix(exp)
    root = ExpTree.make_tree(exp)
    return ExpTree.evaluate(root)


if __name__ == '__main__':
    print('Welcome to Calculator Program!')
    while True:
        ans = input("Please enter your expression here. To quit enter 'quit' or 'q':\n").replace(' ', '')
        # ans = '(A+B)*C-D'#  <- for checking errors
        # ans = '9+2/6'
        if ans == 'quit' or ans == 'q':
            break
        print(calculate(ans))

    print('Goodbye!')