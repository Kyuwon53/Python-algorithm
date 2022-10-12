class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        print(self.stack1[-1])

    def pop(self) -> int:
        """
        stack1 : [1 2 3]
        :return:
        """
        pop_object = None
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        pop_object = self.stack2.pop()
        return pop_object

    # def peek(self) -> int:
    #
    # def empty(self) -> bool:


# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def test_push():
    q = MyQueue()
    q.push(1)
    print(q)


test_push()


def test_pop():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)

    assert obj.pop() == 1
    assert obj.pop() == 2
    assert obj.pop() == 3


test_pop()
