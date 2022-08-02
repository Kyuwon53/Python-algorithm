class Node:
    def __init__(self, data, nextNode=None, prevNode=None):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def get_last_node(self, data):
        node = self.head
        while node:
            node = node.nextNode
        return node.data


class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def printReverse(self, node):
        if self.head == None:
            return False
        node.nextNode = self.tail

        while node.data:
            print(node.data)
            node = node.prevNode


node = Node([1, 2, 3, 4, 5, 6, 7])

doubly = DoublyLinkedList(node.data)
DoublyLinkedList.printReverse(doubly, node)
