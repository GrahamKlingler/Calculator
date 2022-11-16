from stack import Stack

operators = {'+', '-', '*', '/', '(', ')', '^'}
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj
        self.right = None
        self.left = None

    def insertLeft(self, new_node):
        if self.left is None:
            self.left = new_node
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t

    def insertRight(self, new_node):
        if self.right is None:
            self.right = new_node
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        try:
            return self.right
        except:
            print('Node has no right child!')
            return None

    def getLeftChild(self):
        try:
            return self.left
        except:
            print('Node has no left child!')
            return None

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        string = f'{self.key}'
        if not self.getRightChild() and not self.getLeftChild():
            return string + '[][]'

        if self.getLeftChild():
            string += '[' + str(self.getLeftChild()) + ']'
        else:
            string += '[]'

        if self.getRightChild():
            string += '[' + str(self.getRightChild()) + ']'
        else:
            string += '[]'

        return string


class ExpTree(BinaryTree):

    @staticmethod
    def alt_make_tree(postfix):
        """Takes a reversed postfix stack and converts it into an expression tree"""
        # create stack for tree nodes
        nodes = Stack()
        # reverse the postfix stack to get first characters of expression first
        postfix = postfix.reverse()
        # loops over the stack until it is empty
        while not postfix.isEmpty():  # for c in postfix:
            c = postfix.pop()
            if c not in operators:
                nodes.push(c)
            else:
                # if c is an operator, create left and right nodes from nodes list, create node from operator and insert them onto the new node
                right = nodes.pop() # BinaryTree(self.nodes.pop())
                left = nodes.pop() # BinaryTree(self.nodes.pop())
                new_node = ExpTree(c)
                new_node.insertRight(right)
                new_node.insertLeft(left)
                # error checking: print(f'node appended:\nroot:{new_node.getRootVal()}\nleft:{new_node.getLeftChild(
                # ).getRootVal()}\nright:{new_node.getRightChild().getRootVal()}')
                # push new node to nodes stack
                nodes.push(new_node)
        # at end of loop, only the root node is left in the stack
        return nodes.pop()

    @staticmethod
    def make_tree(postfix):
        """Takes a postfix stack and converts it into an expression tree"""
        if postfix.isEmpty():
            return

        c = postfix.pop()

        if c not in operators:
            return c

        right = ExpTree.make_tree(postfix)
        left = ExpTree.make_tree(postfix)

        c = ExpTree(c)
        c.insertLeft(left)
        c.insertRight(right)

        return c

    def __str__(self):
        new_str = ''
        # error testing
        # print(f'Recursive call:\n\tCurr: {curr.getRootVal()}\n\tStr: {new_str}')
        # print(type(self.str_rec(curr, new_str)), type(curr.getRootVal()), type(str))
        if self.left:
            new_str += str(self.left)
        if self.right:
            new_str += str(self.right)
        return new_str + self.getRootVal()

    @staticmethod
    def evaluate(root):
        # base case
        if not isinstance(root, ExpTree):
            return float(root)

        # secondary case
        if root.right is None and root.left is None:
            return float(root.getRootVal())

        # recursive calls to left and right
        left_sum = ExpTree.evaluate(root.left)
        right_sum = ExpTree.evaluate(root.right)

        # check for operator
        if root.getRootVal() == '+':
            return left_sum + right_sum
        elif root.getRootVal() == '-':
            return left_sum - right_sum
        elif root.getRootVal() == '*':
            return left_sum * right_sum
        elif root.getRootVal() == '/':
            return left_sum / right_sum
        else:
            return left_sum ** right_sum

    @staticmethod
    def postorder(root):
        # base case
        if root is None:
            return ''

        # secondary case
        if root.right is None and root.left is None:
            return root.getRootVal()

        # recursive calls
        first_part = ExpTree.postorder(root.left)
        second_part = ExpTree.postorder(root.right)

        return f'{first_part}{second_part}{root.getRootVal()}'

    @staticmethod
    def preorder(root):
        # base case
        if not isinstance(root, ExpTree):
            return root

        # secondary case
        if root.right is None and root.left is None:
            return root.getRootVal()

        # recursive call
        right_sum = ExpTree.preorder(root.right)
        left_sum = ExpTree.preorder(root.left)

        return f'{root.getRootVal()}{left_sum}{right_sum}'

    @staticmethod
    def inorder(root):
        # base case
        if not isinstance(root, ExpTree):
            return root

        # secondary case
        if root.right is None and root.left is None:
            return root.getRootVal()

        # recursive calls
        left_sum = ExpTree.inorder(root.left)
        right_sum = ExpTree.inorder(root.right)
        if isinstance(root.left, ExpTree) and root.left.getRootVal() in operators and priority[root.left.getRootVal()] < priority[root.getRootVal()]:
            left_sum = f'({left_sum})'
        if isinstance(root.right, ExpTree) and root.right.getRootVal() in operators and priority[root.right.getRootVal()] < priority[root.getRootVal()]:
            right_sum = f'({right_sum})'

        return f'{left_sum}{root.getRootVal()}{right_sum}'




