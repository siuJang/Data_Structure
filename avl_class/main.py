from avl_class import *

acl = AVLTree()
root = None

items = [43, 49, 84]
for item in items:
    root = avl.insert(item)

avl.levelOrder(root)