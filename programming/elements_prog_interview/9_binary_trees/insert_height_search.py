class Node:
    def __init__(self, vlaue=None):
        self.value = vlaue
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print('Value already exists')

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
        else:
            return 0

    def _print_tree(self, cur_node):
        if cur_node:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, cur_node, height):
        if cur_node == None:
            return height
        left_height = self._height(cur_node.left, height+1)
        right_height = self._height(cur_node.right, height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root == None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, cur_node):
        if cur_node.value == value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._search(value, cur_node.right)
        return False


if __name__ == '__main__':
    # creat tree
    tree = BinarySearchTree()
    tree.root = Node(10)
    tree.insert(3)
    tree.insert(4)
    tree.insert(29)
    tree.insert(0)
    tree.insert(20)

    print('\nTree... ')
    tree.print_tree()

    print('\nSearch for 25 and 20 ... ')
    print(tree.search(25))
    print(tree.search(20))

    print('\nHeight of the tree...')
    print(tree.height())

