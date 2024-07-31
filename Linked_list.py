
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, index, data):
        if index == 0:
            self.push(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError
            current = current.next
        if current is None:
            raise IndexError
        new_node.next = current.next
        current.next = new_node

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.append(31)
    linked_list.insert(1, 2)
    linked_list.print()  # Output: 1 2 3

