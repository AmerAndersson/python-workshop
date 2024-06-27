"""
class Node 
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def find(self, target) -> None:
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def delete(self, target) -> None:
        node_to_delete = self.find(target=target)
        if node_to_delete:
            if node_to_delete.prev:
                node_to_delete.prev.next = node_to_delete.next
            else:
                self.head = node_to_delete.next
            if node_to_delete.next:
                node_to_delete.next.prev = node_to_delete.prev
            del node_to_delete
