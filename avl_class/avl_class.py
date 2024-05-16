def inorder(self, node):
    if node:
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)


def levelOrder(self, root):
    if root is None:
        return 0

    queue = deque([root])
    cnt = 0
    while queue:
        size = len(queue)

        cnt = cnt + 1
        print(f"★ LEVEL ", cnt, ": ", end="")
        for _ in range(size):
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    return