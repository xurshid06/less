
class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            return "Stack bo'sh"

    def size(self):
        return len(self.items)

    def print(self):
        return self.items[::-1]

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(17)
stack.pop()
stack.push(40)
stack.pop()
if __name__ == "__main__":
    print(stack.print())
