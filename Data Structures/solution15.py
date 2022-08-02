class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right


def insert(value, node):
    if value < node.value:
        if node.leftChild is None:
            node.leftChile = TreeNode(value)
        else:
            insert(value, node.rightChild)
    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.leftChile)


def search(searchValue, node):
    if node is None or node.value == searchValue:
        return node
    elif searchValue < node.value:
        return search(searchValue, node.leftChild)
    else:
        return search(searchValue, node.rightChild)


def delete(value, node):
    if node is None:
        return None
    elif value < node.value:
        node.leftChild = delete(value, node.leftChild)
        return node
    elif value > node.value:
        node.rightChild = delete(value, node.rightChild)
        return node
    elif value == node.value:
        if node.leftChild is None:
            return node.leftChild
        else:
            node.rightChild = lift(node.rightChild, node)
            return node


def lift(node, value):
    if node.leftChild:
        node.leftChild = lift(node.leftChild, value)
        return node
    else:
        value = node.value
        return node.rightChild


node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
print(search(25, root).value)
