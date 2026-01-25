class Treenode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def insert(root, x):
    if root is None:
        return Treenode(x)
    if root.data > x:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root



root = None
root = insert(root, 12)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 34)
root = insert(root, 39)
root = insert(root, 1)
root = insert(root, 23)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")



print("pick one of the 3")

print("1 = inorder")
print("2 = preorder")
print("3 = postorder")

choice = input("enter choice: ")

if choice == "1":
    inorder(root)
elif choice == "2":
    preorder(root)
elif choice == "3":
    postorder(root)
else:
    print("wrong input")
