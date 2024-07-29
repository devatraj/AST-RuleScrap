class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value}, left={self.left}, right={self.right})"
