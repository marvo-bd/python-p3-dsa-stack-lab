class Stack:
    def __init__(self, items=None, limit=100):
        '''Initialize the stack with an optional list of items and a maximum size limit.'''
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        '''Check if the stack is empty.'''
        return len(self.items) == 0

    def push(self, item):
        '''Push an item onto the stack.'''
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        '''Pop an item off the stack.'''
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        '''Peek at the top item of the stack without removing it.'''
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        '''Return the number of items in the stack.'''
        return len(self.items)

    def full(self):
        '''Check if the stack is full based on the limit.'''
        return len(self.items) >= self.limit

    def search(self, target):
        '''Return the index of the target item from the top of the stack.'''
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        return -1
