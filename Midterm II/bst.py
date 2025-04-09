class Node:
    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return '({})'.format(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
        
    def _insert(self, value: int, subtree: Node):
        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)
        else:
            print('Value already exists in tree...')

    def print_pretty(self):
        if self.root is not None:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")

    def _build_tree_string(self, node: Node):
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def find_min(self, subtree: Node) -> Node:
        while subtree.left_child is not None:
            subtree = subtree.left_child
        return subtree  

    def delete(self, value: int):
        if self.root is not None:
            self.root = self._delete(value, self.root)

    def _delete(self, value: int, node: Node) -> Node:
        if node is None:
            return None
        
        if value < node.data:
            node.left_child = self._delete(value, node.left_child)
        elif value > node.data:
            node.right_child = self._delete(value, node.right_child)
        else:
  
            if node.left_child is None and node.right_child is None:
                return None

            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child

            successor = self.find_min(node.right_child)
            node.data = successor.data
            node.right_child = self._delete(successor.data, node.right_child)
        
        return node

    def search(self, value: int) -> Node:
        return self._search(value, self.root)

    def _search(self, value: int, node: Node) -> Node:
        if node is None or node.data == value:
            return node

        if value < node.data:
            return self._search(value, node.left_child)

        return self._search(value, node.right_child)
