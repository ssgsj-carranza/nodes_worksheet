class BinarySearchTree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert_value(self, data):
        if not self.data:
            self.data = data
            return
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.insert_value(data)
                return
            self.left = BinarySearchTree(data)
            return
        if self.right:
            self.right.insert_value(data)
            return
        self.right = BinarySearchTree(data)

    def search(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(data)
        if self.right is None:
            return False
        else:
            return self.right.search(data)


