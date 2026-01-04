class Tree:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.Right = None
root =Tree(1)
root.left=Tree(2)
root.Right=Tree(3)
root.left.left=Tree(4)
root.Right.Right=Tree(5)
root.Right.left=Tree(6)

def preorder(node):
    print (node.data)
    if node.left != None:
        preorder (node.left)
    if node.Right != None:
        preorder (node.Right)
# preorder (root)

def postorder (node):
    if node.left != None:
        postorder (node.left)
    if node.Right != None:
        postorder (node.Right)
    print (node.data)
# postorder (root)

def inorder (node):
    if node.left != None:
        inorder (node.left)
    print (node.data)
    if node.Right != None:
        inorder (node.Right)

inorder (root)