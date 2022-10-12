class SetOfStacks:
    def __int__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.is_empty():
            print("stack is Empty")
        else:
            pop_object = self.stack.pop()
        return pop_object

    def top(self):
        top_object = None
        if self.is_empty():
            print("stack is Empty")
        else:
            top_object = self.stack[-1]
        return top_object

    def empty(self):
        return self.is_empty()

    def __is_empty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty
