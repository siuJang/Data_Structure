from collections import deque
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_recursive(self.root, data)

    def insert_recursive(self, node, data):
        if node is None:
            return TreeNode(data)

        if data < node.val:
            node.left = self.insert_recursive(node.left, data)
            pass
        elif data > node.val:
            node.right = self.insert_recursive(node.right, data)
            pass
        else: #### 입력된 값과 해당 노드 값이 같을 경우
            pass

        return node
    def levelOrder_print(self):
        if self.root is None:
            return 0

        queue = deque([self.root])
        cnt = 0
        while queue:
            size = len(queue)

            cnt = cnt + 1
            print(f"★ LEVEL ", cnt, ": ", end="")
            for _ in range(size):
                node = queue.popleft()
                print(node.val, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

        return
    def search(self, data):
        return self.search_recursive(self.root, data)

    def search_recursive(self, node, data):
        if node is None or node.val == data:
            return node

        if data < node.val:
            return self.search_recursive(node.left, data)
        else:
            return self.search_recursive(node.right, data)

    def inorder_print(self):
        self.inorder_recursive(self.root)
        print()

    def inorder_recursive(self, node):
        if node:
            self.inorder_recursive(node.left)
            print(node.val, end=' ')
            self.inorder_recursive(node.right)
