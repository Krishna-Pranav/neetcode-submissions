from collections import deque

class Codec:

    def serialize(self, root):

        if not root:
            return "N"

        q = deque([root])
        result = []

        while q:

            node = q.popleft()

            if node is None:
                result.append("N")
                continue

            result.append(str(node.val))

            q.append(node.left)
            q.append(node.right)

        return ",".join(result)

    def deserialize(self, data):

        if data == "N":
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))

        q = deque([root])

        i = 1

        while q:

            node = q.popleft()

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)

            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)

            i += 1

        return root