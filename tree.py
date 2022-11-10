from stack import Stack

operators = {'+', '-', '*', '/', '(', ')', '^'}

class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj
        self.right = None
        self.left = None

    def insertLeft(self, new_node):
        if not isinstance(new_node, BinaryTree):
            if self.left is None:
                self.left = BinaryTree(new_node)
            else:
                t = BinaryTree(new_node)
                t.left = self.left
                self.left = t
        else:
            if self.left is None:
                self.left = new_node
            else:
                t = new_node
                t.left = self.left
                self.left = t

    def insertRight(self, new_node):
        if not isinstance(new_node, BinaryTree):
            if self.right is None:
                self.right = BinaryTree(new_node)
            else:
                t = BinaryTree(new_node)
                t.right = self.right
                self.right = t
        else:
            if self.right is None:
                self.right = new_node
            else:
                t = new_node
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

    def to_str(self):
        string = f'{self.key}'
        if not self.getRightChild() and not self.getLeftChild():
            return string + '[][]'

        if self.getLeftChild():
            string += '[' + self.getLeftChild().to_str() + ']'
        else:
            string += '[]'

        if self.getRightChild():
            string += '[' + self.getRightChild().to_str() + ']'
        else:
            string += '[]'

        return string

    def __str__(self):
        return self.to_str()


class ExpTree(BinaryTree):

    '''def __init__(self, postfix):
        root = ExpTree.make_tree(postfix)
        # print(root.getRootVal(), root.getLeftChild().getRootVal())
        super().__init__(root.getRootVal())
        try:
            self.left = root.getLeftChild()
        except:
            self.insertLeft(None)
        try:
            self.right = root.getRightChild()
        except:
            self.insertRight(None)'''

    # Takes a postfix stack and converts it into an expression tree
    @staticmethod
    def make_tree(postfix):
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
                new_node = BinaryTree(c)
                new_node.insertRight(right)
                new_node.insertLeft(left)
                # error checking: print(f'node appended:\nroot:{new_node.getRootVal()}\nleft:{new_node.getLeftChild(
                # ).getRootVal()}\nright:{new_node.getRightChild().getRootVal()}')
                # push new node to nodes stack
                nodes.push(new_node)
        # at end of loop, only the root node is left in the stack
        return nodes.pop()

    def str_rec(self, curr):
        new_str = ''
        # error testing
        # print(f'Recursive call:\n\tCurr: {curr.getRootVal()}\n\tStr: {new_str}')
        # print(type(self.str_rec(curr, new_str)), type(curr.getRootVal()), type(str))
        if curr.left:
            new_str += self.str_rec(curr.left)
        if curr.right:
            new_str += self.str_rec(curr.right)
        return new_str + curr.getRootVal()

    def __str__(self):
        return self.str_rec(self)

    @staticmethod
    def evaluate(root):
        # base case
        if root is None:
            return 0

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
        if root is None:
            return ''

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
        if root is None:
            return ''

        # secondary case
        if root.right is None and root.left is None:
            return root.getRootVal()

        # recursive calls
        left_sum = ExpTree.inorder(root.left)
        right_sum = ExpTree.inorder(root.right)

        return f'({left_sum}{root.getRootVal()}{right_sum})'




