class Stack:
    """
    Inplement by list:
        - Top is at the end of the list
    """
    def __init__(self):
        self._items = []


    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def peek(self):
        try:
            return self._items[-1]
        except:
            return 'The stack is empty'

    def pop(self):
        return self._items.pop()

    def size(self):
        return len(self._items)



