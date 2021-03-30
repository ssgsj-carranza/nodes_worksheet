from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.head is None:
            self.head = new_node
            return

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    def contains(self, value):
        current_value = self.head
        while current_value is not None:
            if current_value.data == value:
                return True
            else:
                return False

