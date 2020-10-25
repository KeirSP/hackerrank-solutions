def preOrder(root):
    if root != None:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)