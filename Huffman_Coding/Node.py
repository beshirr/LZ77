class Node:
    def __init__(self, value, character=None):
        self.value = value
        self.character = character
        self.left = None
        self.right = None


def BuildCodes(root: Node):
    codes: dict = {}

    def DFS(current: Node, code: str):
        if current.left is None and current.right is None:
            codes[current.character] = code
            return

        DFS(current.left, code + "0")
        DFS(current.right, code + "1")

    DFS(root, "")

    return codes