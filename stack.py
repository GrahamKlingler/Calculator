class Stack:

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def reverse(self):
        # returns a reversed version of the stack
        new_l = self.items[::-1]
        return Stack(new_l)

    def __str__(self):
        # returns the stack in a string for error checking
        return ''.join([item for item in self.items])

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
