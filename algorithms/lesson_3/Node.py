from __future__ import annotations


class Node:

    def __init__(self, val: int):
        self.value = val
        self.next = None
        self.prev = None

    def pushNext(self, node: Node):
        self.next = node
        node.prev = self

    def pushPrev(self, node: Node):
        self.prev = node
        node.next = self

    def popNode(self):
        self.next = None
        self.prev = None

    def popNext(self):
        self.next = None

    def popPrev(self):
        self.prev = None

    def __repr__(self):
        return f'Node({self.value})'


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, value: int | float):
        if self.tail:
            self.tail.pushNext(Node(value))
            self.tail = self.tail.next
        else:
            self.head = Node(value)
            self.tail = self.head

    def pushleft(self, value: Node):
        if not type(value) is Node:
            return False
        if self.head:
            value.pushNext(self.head)
            self.head = value

    def popleft(self):
        out = self.head
        out.popNode()
        self.head = self.head.next
        self.head.popPrev()
        return out.value

    def popright(self):
        out = self.tail
        self.tail = self.tail.prev
        out.popNode()
        self.tail.popNext()
        return out.value

    def includes(self, query: int | float):
        if not self.tail:
            return False
        current_node = self.head
        while current_node:
            if current_node.value == query:
                return True
            current_node = current_node.next
        return False

    def sort(self):
        if not self.tail or self.tail == self.head:
            return
        flag = True
        while flag:
            current_node = self.head
            flag = False
            while current_node.next:
                if current_node.value > current_node.next.value:
                    current_node.value, current_node.next.value = current_node.next.value, current_node.value
                    flag = True
                current_node = current_node.next

    def reverse(self):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next, current_node.prev = current_node.prev, current_node.next
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def __str__(self):
        out = []
        val = self.head
        while val:
            out.append(str(val.value))
            val = val.next
        return ', '.join(out)

    def __repr__(self):
        out = []
        val = self.head
        while val:
            out.append(str(val.value))
            val = val.next
        return f'LinkedList([{", ".join(out)}])'
